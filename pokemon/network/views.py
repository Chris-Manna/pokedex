import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import csv


from .models import User, Post, Monster


def show_posts(title, request, posts, profile=None):

    # Get current page of posts
    page_index = request.GET.get("page", 1)
    paginator = Paginator(posts, 5)
    page = paginator.page(page_index)

    # Show posts page
    return render(request, "network/index.html", {
        "title": title,
        "page": page,
        "profile": profile,
        "show_new_monster": (
            request.user.is_authenticated and
            (profile is None or profile == request.user)
        ),
        "show_new_post": (
            request.user.is_authenticated and
            (profile is None or profile == request.user)
        )
        
    })


def monster_csv():
  
  pass

def show_monsters(title, request, monsters, profile=None):
    print("inside show_monsters")
    # Get current page of posts
    page_index = request.GET.get("page", 1)
    paginator = Paginator(monsters, 5)
    page = paginator.page(page_index)

    # Show posts page
    return render(request, "network/index.html", {
        "title": title,
        "page": page,
        "profile": profile,
        "show_new_monster": (
            request.user.is_authenticated and
            (profile is None or profile == request.user)
        )
    })


def index(request):
    print('inside index')
    # posts = Post.objects.order_by("-creation_time").all()
    monsters = Monster.objects.order_by("-monster_id").all()
    
    return show_monsters("Monster Deck", request, monsters)


@login_required
def edit(request, post_id):
    if request.method == "PUT":
        # Query for post
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found."}, status=404)

        # Only let the poster edit the post
        if post.poster != request.user:
            return JsonResponse({"error": "Forbidden."}, status=403)

        # Update post body
        data = json.loads(request.body)
        post.content = data["content"]
        post.save()
        return JsonResponse({
            "id": post_id,
            "content": post.content,
        })


@login_required
def follow(request, username):
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User does not exist.") 
        if user != request.user:
            user.followers.add(request.user)
    return HttpResponseRedirect(reverse("user", args=(username,)))


@login_required
def following(request):
    posts = Post.objects.filter(poster__in=request.user.following.all()).order_by("-creation_time").all()
    return show_posts("Following", request, posts)


@login_required
def new_post(request):
    if request.method == "POST":
        p = Post(
            content=request.POST["content"],
            poster=request.user
        )
        p.save()
        return HttpResponseRedirect(
            request.META.get("HTTP_REFERER", reverse("index"))
        )


@login_required
def new_monster(request):
    if request.method == "POST":
        monster = Monster(
            monster_id =request.POST["monster_id"],
            name =request.POST["name"],
            types =request.POST["types"],
            weaknesses =request.POST["weaknesses"],
            trainer =request.POST["trainer"],
            evolutions =request.POST["evolutions"],
        )
        monster.save()
        return HttpResponseRedirect(
            request.META.get("HTTP_REFERER", reverse("index"))
        )


@login_required
def monster_csv(request):
    if request.method == "POST":
      if request.method == 'POST' and request.FILES['monster_file']:
        monster_file = request.FILES['monster_file']
        decoded_file = monster_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for monster_row in reader:
          monster_id = monster_row['ID']
          name = monster_row['Name']
          types = monster_row['Types']
          weaknesses = monster_row['Weaknesses']
          evolutions = monster_row['Evolution']
          monster = Monster(
            monster_id=monster_id, 
            name=name, 
            types=types, 
            weaknesses=weaknesses, 
            evolutions=evolutions,
            trainer=request.user
            )
          monster.save()
        return HttpResponseRedirect(
            request.META.get("HTTP_REFERER", reverse("index"))
        )


@login_required
def post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    return JsonResponse({
        "id": post_id,
        "content": post.content,
    })


@login_required
def monster(request, monster_id):
    try:
        monster = Monster.objects.get(pk=monster_id)
    except Monster.DoesNotExist:
        return JsonResponse({"error": "Monster not found."}, status=404)
    # evolutions_list = monster.evolutions.split(",")
    # print(f"evolutions_list: {evolutions_list}")
    # all_evolutions = dfs(evolutions)
    return JsonResponse({
        "id": monster_id,
        "monster_id":monster.monster_id,
        "trainer": monster.trainer,
        "types":monster.types,
        "weaknesses":monster.weaknesses,
        # "evolutions":all_evolutions,
    })


@login_required
def unfollow(request, username):
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User does not exist.") 
        if user != request.user:
            user.followers.remove(request.user)
    return HttpResponseRedirect(reverse("user", args=(username,)))


def user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    monsters = Monster.objects.filter(trainer=user).order_by("-monster_id").all()
    return show_posts(user.username, request, monsters, profile=user)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
