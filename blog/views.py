from urllib import request
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, UserProfile, User, Follow
from .forms import RegisterForm, PostForm, CommentForm, ProfileUpdateForm

# Create your views here.
def home(request):

    query = request.GET.get('q')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query) |
            Q(author__username__icontains=query)
        )

    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'query': query
    })

# Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Create Post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Post Detail
def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)

    comments = Comment.objects.filter(post=post)

    is_following = False

    if request.user.is_authenticated:

        is_following = Follow.objects.filter(
            follower=request.user,
            following=post.author
        ).exists()

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=pk)

    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {

        'post': post,
        'comments': comments,
        'form': form,
        'is_following': is_following,
    })
        
# Delete Post
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.author == request.user or request.user.is_staff:
        post.delete()
    return redirect('home')

# Like Post
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    already_liked = Like.objects.filter(user=request.user, post=post)
    if already_liked:
        already_liked.delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect('home')

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user != comment.user and not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {
        'form': form
    })

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user == comment.user or request.user.is_staff:
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', pk=post_id)
    return redirect('home')

def profile(request, username):

    profile_user = User.objects.get(username=username)

    profile, created = UserProfile.objects.get_or_create(
        user=profile_user
    )

    posts = Post.objects.filter(author=profile_user)

    is_following = False

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    if request.user.is_authenticated:

        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(request, 'profile.html', {

        'profile_user': profile_user,
        'profile': profile,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    })
@login_required
def follow_user(request, username):
    target_user = User.objects.get(username=username)
    if request.user != target_user:
        follow = Follow.objects.filter(
            follower=request.user,
            following=target_user
        )
        if follow.exists():
            follow.delete()
        else:
            Follow.objects.create(
                follower=request.user,
                following=target_user
            )
    return redirect('profile', username=username)

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect(
                'profile',
                username=request.user.username
            )
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'edit_profile.html', {
        'form': form
    })