/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./application/templates/*",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}