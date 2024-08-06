/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/*.html"],
  theme: {
    extend: {
      colors: {
        'light-shade':'#E3EAEB',
        'light-accent':'#8797BD',
        'main-colour':'#586292',
        'dark-accent':'#7D86A5',
        'dark-shades':'#12192B',
      }
    },
  },
  plugins: ["flowbite/plugin",],
}

