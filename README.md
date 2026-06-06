# Dominion Randomizer

A lightweight, client-side web application for generating random, balanced Kingdoms for the board game **Dominion**.

## Features

- **Dynamic Generation:** Randomly generates a set of 10 Kingdom cards based on selected expansions.
- **Thematic Generation:** Force specific biases such as "Engine", "Attack & Defense", or "Big Money".
- **Protection Rule:** Automatically swaps in a Reaction card if an Attack card is generated.
- **Card Info Hub:** View every possible card, its cost, type, and extended explanations, and filter by your current Kingdom.
- **Full Dutch Translation:** Play in either English or Dutch. Toggling the language switch completely localizes all UI components, card names, and card descriptions instantly.
- **Mobile Responsive:** Designed to run flawlessly on your phone during game night.

## Local Usage

This project uses standard HTML, CSS, and vanilla JavaScript. There is no build step or server required!
To run it locally, simply double-click the `index.html` file to open it in your web browser. 

> *Note: For the best experience, ensure you have an active internet connection so the app can fetch the latest card database.*

## Hosting on GitHub Pages (Rendered Version)

Because this app consists entirely of static files (`index.html` and `nl_translations.js`), it is incredibly easy to host for free on GitHub so anyone can access it via a public URL.

To get a rendered version running on GitHub:

1. Push this repository to your GitHub account.
2. In your GitHub repository, click on the **Settings** tab.
3. On the left sidebar, click on **Pages**.
4. Under the **Build and deployment** section:
   - Ensure the Source is set to **Deploy from a branch**.
   - Under the **Branch** dropdown, select your main branch (e.g., `main` or `master`) and leave the folder as `/ (root)`.
5. Click **Save**.
6. Wait about 1-2 minutes. GitHub will provide you with a live URL at the top of the Pages settings page (e.g., `https://<your-username>.github.io/<repo-name>/`). 
7. You can now visit this URL on your phone or share it with friends to use the randomizer anywhere!
