/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/*.html"],
  theme: {
    extend: {
      colors: {
        'light-shade':'#F9F9F8',
        'light-accent':'#B2B1AA',
        'main-colour':'#7E91A2',
        'dark-accent':'#959BA6',
        'dark-shades':'#3B373A',
      }
    },
  },
  plugins: ["flowbite/plugin",],
}

