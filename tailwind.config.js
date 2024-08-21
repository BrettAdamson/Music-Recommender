/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/*.html"],
  theme: {
    extend: {
      colors: {
        'light-shade':'#F6F3F2',
        'light-accent':'#B39F6C',
        'main-colour':'#8F9AA6',
        'dark-accent':'#83737E',
        'dark-shades':'#293D4F',
      }
    },
  },
  plugins: ["flowbite/plugin",],
}

