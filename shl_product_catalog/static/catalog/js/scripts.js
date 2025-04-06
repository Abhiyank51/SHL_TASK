document.addEventListener("DOMContentLoaded", function() {
    // Skills input handling
    const skillInput = document.getElementById("skill-input");
    const skillsList = document.getElementById("skills-list");
    const hiddenSkillsInput = document.getElementById("skills");
    let skills = [];

    if (skillInput) {
        skillInput.addEventListener("keypress", function(e) {
            if (e.key === "Enter" && this.value.trim()) {
                e.preventDefault();
                addSkill(this.value.trim());
                this.value = "";
            }
        });
    }

    function addSkill(skill) {
        if (!skills.includes(skill)) {
            skills.push(skill);
            updateSkillsList();
            updateHiddenInput();
        }
    }

    function removeSkill(skill) {
        skills = skills.filter(s => s !== skill);
        updateSkillsList();
        updateHiddenInput();
    }

    function updateSkillsList() {
        skillsList.innerHTML = "";
        skills.forEach(skill => {
            const tag = document.createElement("div");
            tag.className = "skill-tag";
            tag.innerHTML = `${skill} <span class="remove-skill" data-skill="${skill}">✕</span>`;
            skillsList.appendChild(tag);
        });

        skillsList.querySelectorAll(".remove-skill").forEach(button => {
            button.addEventListener("click", function() {
                removeSkill(this.getAttribute("data-skill"));
            });
        });
    }

    function updateHiddenInput() {
        hiddenSkillsInput.value = skills.join(",");
    }

    // Completion popup handling
    const completeButton = document.getElementById("complete-button");
    const popup = document.getElementById("completion-popup");

    if (completeButton) {
        completeButton.addEventListener("click", function() {
            popup.style.display = "block";
        });
    }
});

function closePopup() {
    const popup = document.getElementById("completion-popup");
    popup.style.display = "none";
    window.location.href = catalogHomeUrl;  // Use the JavaScript variable
}