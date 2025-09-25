# GadgetReview

A React application built using Create React App.

## Prerequisites

Before running the project, make sure you have installed:

* [Node.js](https://nodejs.org/) (v16 or higher recommended)
* [npm](https://www.npmjs.com/) (comes with Node.js)

## Getting Started

Clone the repository and install dependencies:

```bash
git clone git@github.com:Benson-Mwanake/GadgetReview.git
cd client
npm install
```

### Running the App

Start the development server:

```bash
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see the app.

The page reloads automatically when you make changes.

### Building for Production

```bash
npm run build
```

The production-ready files will be generated in the `build/` folder.


## Project Structure

```
client
├── db.json
├── package.json
├── package-lock.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── README.md
└── src
    ├── App.jsx
    ├── components
    │   ├── Navbar.jsx
    │   ├── RatingStars.jsx
    │   └── ReviewCard.jsx
    ├── context
    │   └── AuthContext.js
    ├── forms
    │   ├── AddDeviceForm.jsx
    │   └── ReviewForm.jsx
    ├── index.js
    ├── pages
    │   ├── AddDevicePage.jsx
    │   ├── DeviceDetailPage.jsx
    │   ├── DevicesPage.jsx
    │   ├── HomePage.jsx
    │   ├── Login.jsx
    │   ├── NotFound.jsx
    │   └── Register.jsx
    └── styles.css
```

## Languages & Technologies

* JavaScript (ES6+)
* React
* HTML & CSS

## Notes

* Ensure your backend API is running (e.g., at `http://localhost:5000`) for features like authentication and reviews.
* Keep your `.env` file secure if using environment variables.

## Learn More

* [React Documentation](https://reactjs.org/)
* [Create React App Documentation](https://create-react-app.dev/docs/getting-started/)
