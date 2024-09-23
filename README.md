<img src="https://img.pikbest.com/element_our/20230404/bg/b9b6a4b4227c3.png!sw800" alt="Streamlit Authenticator logo" style="margin-top:50px;width:450px"></img>
**A Skill Navigator module to manage user access in a Streamlit application**

## Table of Contents
- [Quickstart](#1-quickstart)
- [Installation](#2-installation)
- [Creating a configuration file](#3-creating-a-configuration-file)
- [Setup](#4-setup)
- [Creating a login widget](#5-creating-a-login-widget)
- [Authenticating users](#6-authenticating-users)
- [Creating a new user registration widget](#7-creating-a-new-user-registration-widget)
- [Creating a Chatbot widget](#8-Creating-a-Chatbot-widget)
- [Updating the configuration file](#9-updating-the-configuration-file)
### 1. Quickstart

* Check out the [demo app](https://skillnavigator-genai-app.streamlit.app/).


### 2. Installation

Streamlit-Authenticator is distributed via [PyPI](https://pypi.org/project/streamlit-authenticator/):

```python
pip install streamlit
```

Using Streamlit-Authenticator is as simple as importing the module and calling it to verify your user's credentials.

```python
import streamlit as st
import skill_navigator as stauth
```

### 3. Creating a configuration file

* Initially create a YAML configuration file and define your user's credentials: including names, usernames, and passwords (plain text passwords will be hashed automatically).
* In addition, enter a name, random key, and number of days to expiry, for a re-authentication cookie that will be stored on the client's browser to enable password-less re-authentication. If you do not require re-authentication, you may set the number of days to expiry to 0.
* Finally, define a list of pre-authorized emails of users who can register and add their credentials to the configuration file with the use of the **register_user** widget.
* **_Please remember to update the config file (as shown in step 12) after you use the reset_password, register_user, forgot_password, or update_user_details widgets._**

```python
credentials:
  usernames:
    leela:
      email: leela@gmail.com
      failed_login_attempts: 0 # Will be managed automatically
      logged_in: False # Will be managed automatically
      name: John Smith
      password: abc # Will be hashed automatically
     chandu:
      email: rbriggs@gmail.com
      failed_login_attempts: 0 # Will be managed automatically
      logged_in: False # Will be managed automatically
      name: Rebecca Briggs
      password: def # Will be hashed automatically

```

* _Please note that the 'failed_login_attempts' and 'logged_in' fields corresponding to each user's number of failed login attempts and log-in status in the credentials will be added and managed automatically._

### 4. Setup

* Subsequently import the configuration file into your script and create an authentication object.

```python
import yaml
from yaml.loader import SafeLoader

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
```

* Plain text passwords will be hashed automatically by default, however, for a large number of users it is recommended to pre-hash the passwords in the credentials using the **Hasher.hash_passwords** function.
* If you choose to pre-hash the passwords, please set the **auto_hash** parameter in the **Authenticate** class to False.
  
> ### Hasher.hash_passwords
> #### Parameters:
>  - **credentials:** _dict_
>    - The credentials dict with plain text passwords.
> #### Returns:
> - _dict_
>   - The credentials dict with hashed passwords.

> ### Authenticate
> #### Parameters:
>  - **credentials:** _dict_
>    - Provides the usernames, names, passwords, and emails, and other user data.
>  - **cookie_name:** _str_
>    - Specifies the name of the re-authentication cookie stored on the client's browser for password-less re-authentication.
>  - **cookie_key:** _str_
>    - Specifies the key that will be used to hash the signature of the re-authentication cookie.
>  - **cookie_expiry_days:** _float, default 30.0_
>    - Specifies the number of days before the re-authentication cookie automatically expires on the client's browser.
>  - **pre_authorized:** _list, optional, default None_
>    - Provides the list of emails of unregistered users who are authorized to register.
>  - **validator:** _Validator, optional, default None_
>    - Provides a validator object that will check the validity of the username, name, and email fields.
>  - **auto_hash:** _bool, default True_
>    - Automatic hashing requirement for passwords, True: plain text passwords will be hashed automatically, False: plain text passwords will not be hashed automatically.

* **_Please remember to pass the authenticator object to each and every page in a multi-page application as a session state variable._**

### 5. Creating a login widget

* You can render the login widget as follows.

```python
authenticator.login()
```

> ### Authenticate.login
> #### Parameters:
>  - **location:** _str, {'main', 'sidebar', 'unrendered'}, default 'main'_
>    - Specifies the location of the login widget.
>  - **max_concurrent_users:** _int, optional, default None_
>    - Limits the number of concurrent users. If not specified there will be no limit to the number of concurrently logged in users.
>  - **max_login_attempts:** _int, optional, default None_
>    - Limits the number of failed login attempts. If not specified there will be no limit to the number of failed login attempts.
>  - **fields:** _dict, optional, default {'Form name':'Login', 'Username':'Username', 'Password':'Password', 'Login':'Login'}_
>    - Customizes the text of headers, buttons and other fields.
>  - **captcha:** _bool, default False_
>    - Specifies the captcha requirement for the login widget, True: captcha required, False: captcha removed.
>  - **clear_on_submit:** _bool, default False_
>    - Specifies the clear on submit setting, True: clears inputs on submit, False: keeps inputs on submit.
>  - **key:** _str, default 'Login'_
>    - Unique key provided to widget to avoid duplicate WidgetID errors.
>  - **callback:** _callable, optional, default None_
>    - Optional callback function that will be invoked on form submission with a dict as a parameter.
>  - **sleep_time:** _float, optional, default None_
>    - Optional sleep time for the login widget.
> #### Returns:
> - _str_
>   - Name of the authenticated user.
> - _bool_
>   - Status of authentication, None: no credentials entered, False: incorrect credentials, True: correct credentials.
> - _str_
>   - Username of the authenticated user.

![](https://github.com/Leelakrishnamohanbolla7711/HexaNova/blob/main/project_screenshots/Login_page.png?raw=true)

* **_Please remember to re-invoke an 'unrendered' login widget on each and every page in a multi-page application._**

### 6. Authenticating users

* You can then retrieve the name, authentication status, and username from Streamlit's session state using **st.session_state['name']**, **st.session_state['authentication_status']**, and **st.session_state['username']** to allow a verified user to access restricted content.
* You may also render a logout button, or may choose not to render the button if you only need to implement the logout logic programmatically.
* The optional **key** parameter for the logout button should be used with multi-page applications to prevent Streamlit from throwing duplicate key errors.

```python
if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
```

> ### Authenticate.logout
> #### Parameters:
>  - **button_name:** _str, default 'Logout'_
>    - Customizes the button name.
>  - **location:** _str, {'main', 'sidebar', 'unrendered'}, default 'main'_
>    - Specifies the location of the logout button. If 'unrendered' is passed, the logout logic will be executed without rendering the button.
>  - **key:** _str, default None_
>    - Unique key that should be used in multi-page applications.
>  - **callback:** _callable, optional, default None_
>    - Optional callback function that will be invoked on form submission with a dict as a parameter.

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/logged_in.JPG)

* Or prompt an unverified user to enter a correct username and password.

![](https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/graphics/incorrect_login.JPG)

* You may also retrieve the number of failed login attempts a user has made by accessing **st.session_state['failed_login_attempts']** which returns a dictionary with the username as key and the number of failed attempts as the value.


### 7. Creating a new user registration widget

* You may use the **register_user** widget to allow a user to sign up to your application as shown below.
* If you require the user to be pre-authorized, set the **pre_authorization** parameter to True and add their email to the **pre_authorized** list in the configuration file.
* Once they have registered, their email will be automatically removed from the **pre_authorized** list in the configuration file.
* Alternatively, to allow anyone to sign up, set the **pre_authorization** parameter to False.

```python
def signup():
    st.title("🔏 :red[Create An Account]")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    signup_button = st.button(":red[Signup]")

    if signup_button:
    # Validate input (add more checks as needed)
        if not username or not email or not password:
            st.error("Please fill in all fields.")
        else:
            try:
                # Insert data into the database
                c.execute("INSERT INTO signup_data (username, email, password) VALUES (?, ?, ?)", (username, email, password))
                conn.commit()
                # Redirect to success page
                st.success("Signup successful!")
                st.session_state['show_signup'] = False
                st.rerun()
            except sqlite3.IntegrityError:
                st.error("Username or email already exists.")
    st.write("Already have an account?")
    if st.button("Login"):
        st.session_state['show_signup'] = False
        st.rerun()
    conn.close()
```

> ### Authenticate.register_user
> #### Parameters:
>  - **location:** _str, {'main', 'sidebar'}, default 'main'_
>    - Specifies the location of the register user widget.
>  - **pre_authorization:** _bool, default True_
>    - Specifies the pre-authorization requirement, True: user must be pre-authorized to register, False: any user can register.
>  - **domains:** _list, optional, default None_
>    - Specifies the required list of domains a new email must belong to i.e. ['gmail.com', 'yahoo.com'], list: the required list of domains, None: any domain is allowed.
>  - **fields:** _dict, optional, default {'Form name':'Register user', 'Email':'Email', 'Username':'Username', 'Password':'Password', 'Repeat password':'Repeat password', 'Register':'Register'}_
>    - Customizes the text of headers, buttons and other fields.
>  - **captcha:** _bool, default True_
>    - Specifies the captcha requirement for the register user widget, True: captcha required, False: captcha removed.
>  - **clear_on_submit:** _bool, default False_
>    - Specifies the clear on submit setting, True: clears inputs on submit, False: keeps inputs on submit.
>  - **key:** _str, default 'Register user'_
>    - Unique key provided to widget to avoid duplicate WidgetID errors.
>  - **callback:** _callable, optional, default None_
>    - Optional callback function that will be invoked on form submission with a dict as a parameter.
> #### Returns:
> - _str_
>   - Email associated with the new user.
> - _str_
>   - Username associated with the new user.
> - _str_
>   - Name associated with the new user.

![](https://github.com/Leelakrishnamohanbolla7711/HexaNova/blob/main/project_screenshots/signup.png?raw=true)

* **_Please remember to update the config file (as shown in step 12) after you use this widget._**

### 8. Creating a Chatbot widget

* You may use the chatbot widget to allow a user to know new information.
* You can ask from prompt anything.
* prompt will respond for the question.

```python
import streamlit as st
from openai import OpenAI

st.title("💬 Skill Navigator Chatbot")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
# # OpenAI API Ke

# # Chatbot prompt using OpenAI
# def chatbot_response(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

# # Chatbot section
# st.title("💬 Skill Navigator Chatbot")
# chatbot_prompt = st.text_input("Ask me anything:")

# if chatbot_prompt:
#     with st.spinner('Thinking...'):
#         response = chatbot_response(chatbot_prompt)
#         st.write(response)

```



![](https://github.com/Leelakrishnamohanbolla7711/HexaNova/blob/main/project_screenshots/Chatbot_image.jpg?raw=true)

* **_Please remember to update the config file (as shown in step 12) after you use this widget._**


### 9. Updating the configuration file

* Please ensure that the configuration file is re-saved anytime the credentials are updated or whenever the **reset_password**, **register_user**, **forgot_password**, or **update_user_details** widgets are used.

```python
with open('../config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
```

