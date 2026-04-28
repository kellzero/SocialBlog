
const API_URL = '/api';
let authToken = localStorage.getItem('token');

async function register(username, email, password, password2) {
    const response = await fetch(`${API_URL}/accounts/register/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password, password2 })
    });
    return await response.json();
}

async function login(username, password) {
    const response = await fetch(`${API_URL}/accounts/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    if (data.token) {
        authToken = data.token;
        localStorage.setItem('token', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));
    }
    return data;
}

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    authToken = null;
    window.location.href = '/login/';
}

async function getFeed() {
    const response = await fetch(`${API_URL}/posts/posts/feed/`, {
        headers: { 'Authorization': `Token ${authToken}` }
    });
    return await response.json();
}

async function createPost(content) {
    const response = await fetch(`${API_URL}/posts/posts/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token ${authToken}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content })
    });
    return await response.json();
}

async function likePost(postId) {
    const response = await fetch(`${API_URL}/posts/posts/${postId}/like/`, {
        method: 'POST',
        headers: { 'Authorization': `Token ${authToken}` }
    });
    return await response.json();
}

async function unlikePost(postId) {
    const response = await fetch(`${API_URL}/posts/posts/${postId}/unlike/`, {
        method: 'POST',
        headers: { 'Authorization': `Token ${authToken}` }
    });
    return await response.json();
}

async function addComment(postId, content) {
    const response = await fetch(`${API_URL}/posts/posts/${postId}/add_comment/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token ${authToken}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content })
    });
    return await response.json();
}

async function getUsers() {
    const response = await fetch(`${API_URL}/accounts/users/`, {
        headers: { 'Authorization': `Token ${authToken}` }
    });
    return await response.json();
}

function isAuthenticated() {
    return authToken !== null;
}

function getUser() {
    return JSON.parse(localStorage.getItem('user') || '{}');
}
let avatarUrl = user.profile?.avatar;
if (!avatarUrl || avatarUrl.includes('default')) {
    avatarUrl = '/static/default-avatar.jpg';
}
document.getElementById('navAvatar').src = avatarUrl;