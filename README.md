# Terminal OTP

A terminal authenticator app that can be used to perform 2FA on for GitHub.

![image](https://github.com/ashleendaly/terminal-otp/assets/54708608/8dc5b8ff-9a45-4ef7-8ee6-78facec808a5)

## Usage

1. Clone repository
2. Make sure you have [poetry](https://python-poetry.org/) installed on your system.
3. Run `poetry install`
4. Go to GitHub settings > Password and authentication > Two-factor authentication > Two-factor methods > Authenticator App > **Edit**
5. Click on the setup key link:

   ![image](https://github.com/ashleendaly/terminal-otp/assets/54708608/d32371e9-b349-4da8-bdc0-348e68fdac69)

6. Copy the secret key
7. Create a `.env` file in the root of the project repository and paste the secret key in as shown: `GH_SECRET="******"`
8. Run `make run`
