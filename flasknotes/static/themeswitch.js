const toggleThemeBtn = document.querySelector('#toggle-theme');

toggleThemeBtn.addEventListener('click', function() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  });

  function myfunction(e) {
  console.log("you clicked");
  document.documentElement.classList.toggle("dark-mode");
  document.querySelectorAll(".inverted").forEach((result) => {
    result.classList.toggle("invert");
  });
}
const btn = document.querySelector('.btn')
btn.addEventListener('click', myfunction);


