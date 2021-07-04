console.log("register connected!");

const usernameField = document.querySelector("#usernameField");
const usernameFeedback = document.querySelector(".invalid-feedback");
const emailField = document.querySelector("#emailField");
const emailFeedback = document.querySelector(".email-feedback");

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

if (emailField) {
  emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;
    emailField.classList.remove("is-invalid");
    emailFeedback.style.display = "none";

    if (emailVal.length > 0) {
      fetch("/auth/validate-email", {
        body: JSON.stringify({ email: emailVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (data.email_error) {
            emailField.classList.add("is-invalid");
            emailFeedback.style.display = "block";
            emailFeedback.innerHTML = `<p>${data.email_error}</p>`;
          }
        });
    }
  });
}
