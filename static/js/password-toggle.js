      function addPasswordToggle(inputId) {
        const passwordInput = document.getElementById(inputId)
      
        if (passwordInput) {
          const parent = passwordInput.parentElement
      
          const toggleButton = document.createElement('button')
          toggleButton.type = 'button'
          toggleButton.innerHTML = '<i class="fa-solid fa-eye"></i>'
          toggleButton.setAttribute('aria-label', 'Show password')
      
          const inputWrapper = document.createElement('div')
          inputWrapper.style.position = 'relative'
          inputWrapper.style.width = '100%'
      
          passwordInput.style.width = '100%'
          passwordInput.style.paddingRight = '45px'
      
          toggleButton.style.position = 'absolute'
          toggleButton.style.right = '12px'
          toggleButton.style.top = '50%'
          toggleButton.style.transform = 'translateY(-50%)'
          toggleButton.style.background = 'transparent'
          toggleButton.style.border = 'none'
          toggleButton.style.cursor = 'pointer'
          toggleButton.style.color = '#2563eb'
          toggleButton.style.fontSize = '16px'
      
          inputWrapper.appendChild(passwordInput)
          inputWrapper.appendChild(toggleButton)
          parent.appendChild(inputWrapper)
      
          toggleButton.addEventListener('click', () => {
            if (passwordInput.type === 'password') {
              passwordInput.type = 'text'
              toggleButton.innerHTML = '<i class="fa-solid fa-eye-slash"></i>'
              toggleButton.setAttribute('aria-label', 'Hide password')
            } else {
              passwordInput.type = 'password'
              toggleButton.innerHTML = '<i class="fa-solid fa-eye"></i>'
              toggleButton.setAttribute('aria-label', 'Show password')
            }
          })
        }
      }