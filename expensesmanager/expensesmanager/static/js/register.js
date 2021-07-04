console.log("register working!");

const usernameField = document.querySelector("#usernameField");
if (usernameField) {
  usernameField.addEventListener("keyup", () => {
    console.log("keyup! 323");
  });
}
