// Generate a random OTP
function generateOTP(length) {
    var characters = '0123456789';
    var otp = '';
    for (var i = 0; i < length; i++) {
      otp += characters[Math.floor(Math.random() * characters.length)];
    }
    return otp;
  }
  
  // Send the OTP to the user's phone number
  function sendOTP() {
    var phoneNumber = document.getElementById('phone-number').value;
    var otp = generateOTP(6);
   
    console.log('OTP: ' + otp);
  }
  
  // Verify the OTP entered by the user
  function verifyOTP() {
    var enteredOTP = document.getElementById('otp').value;
    var generatedOTP = 123467;
    if (enteredOTP === generatedOTP) {
      console.log('OTP verified successfully');
    } else {
      console.log('Invalid OTP. Please try again.');
      // Display an error message to the user and prompt them to enter the OTP again
    }
  }
  