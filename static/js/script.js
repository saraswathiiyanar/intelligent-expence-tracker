// Display welcome message
window.onload = function () {
    console.log("Expense Tracker Loaded Successfully");
};

// Confirm before deleting an expense
function confirmDelete() {
    return confirm("Are you sure you want to delete this expense?");
}

// Validate expense form
function validateForm() {
    let amount = document.getElementById("amount").value;

    if (amount <= 0) {
        alert("Please enter a valid amount.");
        return false;
    }

    return true;
}

// Show financial advice alert
function showAdvice(message) {
    alert("Financial Advice: " + message);
}