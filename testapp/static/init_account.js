
let ACCSTORAGE = "acc_id";
let accountId = localStorage.getItem(ACCSTORAGE);

if (accountId == null){
    console.log("No account creating one.");
    localStorage.setItem(ACCSTORAGE, "someid");
} else {
    console.log("Detected an account.")
}
