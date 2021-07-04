console.log("register connected!");

const usernameField = document.querySelector("#usernameField");
const usernameFeedback = document.querySelector(".invalid-feedback");

if (usernameField) {
  usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;
    usernameField.classList.remove("is-invalid");
    usernameFeedback.style.display = "none";

    if (usernameVal.length > 0) {
      fetch("/auth/validate-username", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (data.username_error) {
            usernameField.classList.add("is-invalid");
            usernameFeedback.style.display = "block";
            usernameFeedback.innerHTML = `<p>${data.username_error}</p>`;
          }
        });
    }
  });
}
