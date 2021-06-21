# Columnar Transposition Cipher in Python 👨‍💻

This is an example of Columnar Transposition Cipher in python. This project uses **matrixes** to hash a string.

---

## Usage 📜

The project requires _no dependencies_. So getting started is as easy as,

1. Clone the repository
2. Open the `main.py` file
3. Edit the variables under the comments those state which ones to change.

---

## _Columnar Transposition_ Cipher for beginners ✨

It's an old cipher used in the **past**. It's really **simple**.

The plain text will be referred to as "string to hash" from now on.
The string to hash will be `"Hello world!"` for now. First, we will create a grid with a breadth of 5 characters and length `N`, and fill it with the characters in the string to hash.

---

|  1  |  2  |  3  |  4  |  5  |
| :-: | :-: | :-: | :-: | :-: |
|  H  |  E  |  L  |  L  |  O  |
|     |  W  |  O  |  R  |  L  |
|  D  |  !  |     |     |     |

---

The above table is then converted to the hash by just writing the content from bottom to top, so the result will be `'d H!we ol rl lo'`.

To learn more about this type of transposition cipher go to [wiki](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition).

---

## Contributing 🎉

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

#### Created by Aadhi with 💗
