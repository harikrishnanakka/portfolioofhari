document.querySelector('#contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    e.target.elements.name.value = '';
    e.target.elements.email.value = '';
    e.target.elements.message.value = '';
  });
 // Function to show the success message
 function showSuccessMessage() {
  var successMessage = document.getElementById('success-message');
  successMessage.style.display = 'block';

  // You can add further logic here, e.g., redirect after a delay
  // window.location.href = '/redirect-url';
}

// Add an event listener to the form submission
document.getElementById('contact-form').addEventListener('submit', function (event) {
  // Prevent the default form submission
  event.preventDefault();

  // Your existing AJAX submission logic (you can use Fetch API or jQuery.ajax)
  // After a successful submission, call the showSuccessMessage function
  // For simplicity, I'm calling it after a timeout here
  setTimeout(showSuccessMessage, 1000);
});