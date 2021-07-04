console.log("register connected!");

const usernameField = document.querySelector("#usernameField");
if (usernameField) {
  usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;
    // console.log(usernameVal);
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
          }
        });
    }
  });
}
