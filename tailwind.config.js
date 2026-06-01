/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  // content: [],
  theme: {
    extend: {
      fontFamily: {
				heading: ['Montserrat', 'sans-serif'],
				sans: ['Mulish', 'sans-serif']
			},
			colors: {
				primary: '#006AFF',
				black: '#141516'
			}
    },
  },
  plugins: [],
}

