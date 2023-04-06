document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('register-form');
  const errorMessages = form.querySelectorAll('.error-message');
  
  form.addEventListener('submit', async (event) => {
      event.preventDefault();
  
      const formData = new FormData(form);
      const response = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: {
              'X-Requested-With': 'XMLHttpRequest',
          },
      });
  
      const data = await response.json();
  
      if (data.status === 'error') {
          errorMessages.forEach((errorMessage) => {
              const inputName = errorMessage.dataset.inputName;
              const errorText = data.errors[inputName] || '';
  
              errorMessage.textContent = errorText;
              errorMessage.style.display = errorText ? 'block' : 'none';
          });
      } else {
          // Redirect to the homepage or desired page after successful registration
          window.location.href = '/';
      }
  });
});
