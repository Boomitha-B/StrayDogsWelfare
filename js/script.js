// --- TOAST NOTIFICATION SYSTEM ---
function createToastContainer() {
    if (!document.getElementById('toast-container')) {
        const container = document.createElement('div');
        container.id = 'toast-container';
        container.style.position = 'fixed';
        container.style.top = '20px';
        container.style.right = '20px';
        container.style.zIndex = '10000';
        document.body.appendChild(container); // Append to body
    }
}

function showToast(message, type = 'success') {
    createToastContainer();
    const container = document.getElementById('toast-container');

    const toast = document.createElement('div');
    toast.className = `toast ${type} show`;
    toast.textContent = message;

    // Ensure styles are applied if CSS didn't load slightly (fallback)
    // But reliance on style.css is better. We added .toast css earlier.

    container.appendChild(toast);

    // Remove after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 400); // Wait for fade out
    }, 3000);
}

// --- VALIDATION HELPERS ---

function validateName(name) {
    // Allows alphabets and spaces only
    const regex = /^[A-Za-z\s]+$/;
    return regex.test(name);
}

function validatePhone(phone) {
    // Allows exact 10 digits
    const regex = /^\d{10}$/;
    return regex.test(phone);
}

// --- FORM HANDLING ---

async function handleFormSubmit(event, url, getPayload, validationRules = {}) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    // 1. Check Required Fields (Generic)
    for (let [key, value] of formData.entries()) {
        if (!value.trim()) {
            showToast(`Please fill the ${key.replace('_', ' ')} field.`, 'error');
            return;
        }
    }

    // 2. Specific Validation
    if (validationRules.nameField && !validateName(formData.get(validationRules.nameField))) {
        showToast('Name must contain only alphabets.', 'error');
        return;
    }

    if (validationRules.phoneField && !validatePhone(formData.get(validationRules.phoneField))) {
        showToast('Phone number must be exactly 10 digits.', 'error');
        return;
    }

    // 3. Prepare Payload
    const payload = getPayload(formData);

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();
        if (response.ok) {
            showToast(result.message || 'Submitted Successfully!', 'success');
            form.reset();
        } else {
            showToast(result.error || 'Something went wrong.', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Failed to connect to the server.', 'error');
    }
}

document.addEventListener('DOMContentLoaded', () => {

    // 1. Contact Form
    const contactPageForm = document.getElementById('contactForm');
    if (contactPageForm) {
        contactPageForm.addEventListener('submit', (e) => {
            handleFormSubmit(e, '/api/contact',
                (formData) => ({
                    name: formData.get('name'),
                    email: formData.get('email'),
                    message: formData.get('message')
                }),
                { nameField: 'name' } // Validate Name
            );
        });
    }

    // 2. Donate Form
    const donatePageForm = document.getElementById('donateForm');
    if (donatePageForm) {
        donatePageForm.addEventListener('submit', (e) => {
            handleFormSubmit(e, '/api/donate',
                (formData) => ({
                    donor_name: formData.get('name'),
                    email: formData.get('email'),
                    amount: formData.get('amount')
                }),
                { nameField: 'name' } // Validate Donor Name
            );
        });
    }

    // 3. Volunteer Form
    const volunteerPageForm = document.getElementById('volunteerForm');
    if (volunteerPageForm) {
        volunteerPageForm.addEventListener('submit', (e) => {
            handleFormSubmit(e, '/api/volunteer',
                (formData) => ({
                    name: formData.get('name'),
                    email: formData.get('email'),
                    phone: formData.get('phone'),
                    interest: formData.get('interest')
                }),
                { nameField: 'name', phoneField: 'phone' } // Validate Name and Phone
            );
        });
    }

    // 4. Rescue Form
    const rescueForm = document.getElementById('rescueForm');
    if (rescueForm) {
        rescueForm.addEventListener('submit', (e) => {
            handleFormSubmit(e, '/api/rescue',
                (formData) => ({
                    reporter_name: formData.get('reporter_name'),
                    contact_number: formData.get('contact_number'),
                    location: formData.get('location'),
                    description: formData.get('description')
                }),
                { nameField: 'reporter_name', phoneField: 'contact_number' } // Validate Reporter Name and Contact
            );
        });
    }

    // 5. Adoption Form
    const adoptionForm = document.getElementById('adoptionForm');
    if (adoptionForm) {
        adoptionForm.addEventListener('submit', (e) => {
            handleFormSubmit(e, '/api/adoption',
                (formData) => ({
                    applicant_name: formData.get('applicant_name'),
                    email: formData.get('email'),
                    dog_name: formData.get('dog_name')
                }),
                { nameField: 'applicant_name' } // Validate Applicant Name
            );
        });
    }

});
