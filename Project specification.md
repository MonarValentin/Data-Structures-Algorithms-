Functional Specification for Trackpath

Table of Contents - To be added in later

1.  Introduction

1.1 Overview

The app being designed is called ‘Trackpath’ which is best described as a
fitness app. The app will automatically track the users steps and activity
throughout the day. The application’s purpose will be to offer a cheaper
alternative to replace the expensive hardware on the market such as Fitbit or
Garmin pedometers. It will provide the same benefits by only carrying your
smartphone around. The app will also show you a map of the routes you have
travelled throughout the day.

The home screen of the app will show steps accumulated, distance travelled,
calories burned and a scrollable timeline.

Trackpath will not only be able to track daily steps but it will also be able to
track your movements throughout the day and provide you with a timeline showing
you where you have been throughout the day.

Example.

9:00 - 9:10 - Walk

9:10 - 9:20 - Costa

9:20 - 9:30 - Walk

9:30 - 10:30 - Office

1.2 Business Context

In the business context of this product there could be two possibilities.

-   Put the app on Google Play Store for free. Put ads on the free version of
    the app. Option to upgrade to the pro version of the app which will be ad
    free and have more features.

-   Selling the product to an external organisation. They could modify the
    product or keep it as it is or they could adapt it to their own product.

1.3 Glossary of terms

-   Java

    -   G[eneral-purpose](https://en.wikipedia.org/wiki/General-purpose_language)
        [programming
        language](https://en.wikipedia.org/wiki/Programming_language) that is
        [class-based](https://en.wikipedia.org/wiki/Class-based_programming),
        [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming),
        and designed to have as few implementation
        [dependencies](https://en.wikipedia.org/wiki/Dependency_(computer_science))
        as possible. It is intended to let [application
        developers](https://en.wikipedia.org/wiki/Application_developer) write
        once, run anywhere.

-   GPS

    -   Global Positioning System

-   Realm

    -   Open source object database management system

Login

logout

1.  General Description

2.1 Product Functions / System Functions

Below is a preliminary list of the main functions which may have extra features
if we think they are worth adding. Each function will be discussed in more
detail in the following section.

-   Sign up

-   Log in\*

-   Log out\*

-   Edit profile\*

-   Count steps

-   Graph - some sort of graph between the days(last 7 days preferably )\*

-   Set goal - minimum daily steps/distance\*

-   Calorie count\*

-   History of places visited(days/weeks/months) \*

-   Maps - showing the route traveled in that particular day\*

*\*Requires LogIn*

2.2 User Characteristics and Objectives

The app will be available for free on the Google Play Store. So anybody with an
Android smartphone will have access to the app. The target audience will be
males and females who are interested in keeping track of their daily steps and
their daily activity throughout the day.

Once the app is downloaded, the app with prompt the user to sign up and create
an account. The user will then be able to create goals that they would like to
reach eg walk 10,000 steps a day or be active for 2 hours.

2.3 Operational Scenarios

For the design of our application there will be three different scenarios under
which the application will perform. The first scenario is where the user is
unregistered and in order to access the application content the user will be
prompted with a Sign Up form or if he already has an account he will be prompted
with a LogIn form.

-   Unregistered User.

>   The unregistered user will only be able to see the application logo and have
>   an option to Sign Up where he will be redirected to complete a form where
>   the first name, last name , age, email and a password will be needed in
>   order to create the account.

-   Register user( not logged in)

>   The user will be asked to enter the email and password chosen in the step
>   above in order to log in.If the login is successful access will be granted
>   else he will be asked to enter the details again.

-   Registered user(logged in)

>   The registered user will be able to see the application logo where and have
>   an option to log in where he will be asked for the email and password
>   provided when the Sign Up form was completed. If the LogIn is successful the
>   user will be allowed to use the application functions

-   *Edit Profile\**

>   This function will allow the user to update their profile details with newer
>   information . In order to access this function the user must have an account
>   and must be logged in.

-   *Set goal\**

>   Where the user can set a goal of steps / distance in order to keep
>   motivated.

-   *Count Steps\**

>   The count steps function will be displayed on the main page and it will
>   automatically display the number of steps taken on that day.

-   *Calorie count\**

>   The user can check the estimated amount of calories burned at the time they
>   access the function.

-   *Graph\**

>   The user will be able to visualise a graph for the last 7 days in order to
>   see how active they have been and in which day they had more steps/distance
>   travelled.

-   *History of visited places\**

>   The user will be able to go to the history of the places the has been since
>   he started using the application. They will come up sorted in chronological
>   order and the user will be able to select certain days/weeks/months and
>   check where they were at the chosen moment.

-   *Maps\**

>   Where the user can display the route that he has travelled in that
>   particular day. With the help with this function the user can see which
>   route has more steps and increase/decrease the steps number by choosing
>   another route.

\**Requires LogIn*

2.4 Constraints

The one real constraints we are really facing are regarding the storage space
and the deadline.

-   *Database Memory*

>   Because we are using the Realm Database we have a limit on the scale we can
>   test this application . We will be unable to test the application on a high
>   scale with multiple users logged in at the same time,where problems may
>   arise in terms of memory.

-   *Time*

>   As this project has the potential to grow and gather a lot of users, the
>   deadline will be there in order to demonstrate the application at a low
>   level where the main functionality is created and not for how the
>   application will evolve in time.

-   *Efficiency*

>   As the application will run in the background in order to calculate the data
>   from the GPS and accelerometer the battery life may drain very fast. In
>   order to calculate the steps the data from the GPS and accelerometer will
>   have to be calculated and we will do our best to make the calculations as
>   fast and precise they can be.

-   *Cloud memory*

>   In order to store the information about the steps/distance travelled and the
>   history of the places visited we will have to store them into the cloud
>   where for now the amount of storage will be limited because we cannot afford
>   paying for full subscription as the packages are very expensive on full
>   version.

3 Functional requirements

3.1 Sign Up

-   *Description*

>   The Sign Up is the first function that a non registered comes across. In
>   order to create an account the user will have to enter some mandatory pieces
>   of data in order to go through to the next step in order to complete the
>   registration process.

-   *Criticality*

>   This function is critical to the whole idea of our application,without it
>   the user wouldn’t be able to have access to the content of the application
>   therefore the user wouldn’t be able to use the application as intended.

-   *Technical Issues*

For a successful Sign Up we will have to check and validate the

email address, and the password will have to be encrypted using

Cypher with a key known just by us before it gets stored in the

Database.

-   *Dependency*

>   None

3.2 LogIn

-   *Description*

>   The login function allows the user to access their newly created account.
>   The login will simply require the email and password provided when the
>   account was created.

-   *Criticality*

>   The login function is very important as without it the user wouldn’t have
>   access to the functionality that the application as to offer.

-   *Technical Issues*

>   The only concerns regarding the login function are regarding the decryption
>   . When the user will enter the password it will query the database which
>   will have to return the decrypted password.

-   *Dependency*

>   The login function is only dependent on the Signup function, in order to
>   login you must have an account created.

3.3 Log out

-   *Description*

>   The logout function will allow the user to exit the application, the
>   application will run in the background and if the user wants to stop it he
>   can simply logout.

-   *Criticality*

>   When the user will choose to logout the application will stop recording any
>   values from the GPS and accelerometer so the steps/distance will stop
>   recording.

-   *Technical issues*

>   If the user does logout he will have to login and enter the details again
>   e.g email and password.

-   *Dependency*

>   This function is dependent on the login function. In order to log out the
>   user must be logged in and all its dependencies.

3.4 Edit Profile

-   *Description*

-   *Criticality*

-   *Technical Issues*

-   *Dependencies*

3.5 Graph

-   *Description*

>   This function will allow the user to see a graph with the steps/distance
>   between the last 7 days. With the help of this function the user can see in
>   which day of the week he was the most active.

-   *Criticality*

>   In order to use the function the user has to have data gathered for the last
>   7 days in order to make the analysis. If the user is missing one of the last
>   7 days then this function will let display an appropriate message informing
>   the user to be logged in every day.

-   *Technical issues*

>   None

-   *Dependency*

>   This functional requirement depends on the log in function and all its
>   dependencies
