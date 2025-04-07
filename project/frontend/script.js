
function loginUser(event) {
  event.preventDefault();
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;
  const storedEmail = localStorage.getItem('userEmail');
  const storedPassword = localStorage.getItem('userPassword');
  if (email === storedEmail && password === storedPassword) {
    window.location.href = 'dashboard.html';
  } else {
    alert('Invalid credentials');
  }
}
function registerUser(event) {
  event.preventDefault();
  const email = document.getElementById('register-email').value;
  const password = document.getElementById('register-password').value;
  localStorage.setItem('userEmail', email);
  localStorage.setItem('userPassword', password);
  alert('Registered! You can login now.');
  window.location.href = 'index.html';
}
