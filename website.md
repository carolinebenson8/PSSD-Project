# Automated Job Searcher Project Website

**KEY NOTES** (DELETE): 
- We have to make this have a good narrative 
- screenshots or pics lets put in a shared drive so that we can easily access to input for website later. for time being label areas where photo will be in italics and bold (** word **)

## THE BIG IDEA
*Quick and easily understandable explanation of what your project is all about. Consider including a narrative or example use case, e.g. via screenshots, video, or story boarding. **(DELETE)***
- need to efficiently find jobs, all college seniors trying to find our next stop on journey called life
  
Our Automated Job Searcher is a simple to use program that emails a user a list of all jobs found on Indeed that meet the position and location criteria given. The idea for the Automated Job Searcher sparked out of the common problem our team could relate to as seniors at Babson college who were either looking for a job or knew others who were searching for a job during 2020's uncertain times. We wanted to make the job hunting process more efficent where we could receive a list of all the jobs that met our position and location requirements, rather than having to spend a clicking through pages of potential jobs and only liking five after all that time. Since this project was to try to automate something to be more efficient this was the perfect project to work on because it could be automated *and* it mattered to us.

## User instructions/ReadMe
**(DELETE)** Information to help users download, install, and get started running your software.*
README FILE THAT WE CREATED.

## Implementation Information
**(DELETE)***Code doesn't tell a story by itself. Use more effective methods such as flowcharts and architectural or class diagrams to explain how your code works. You could consider including or linking to snippets of code to highlight a particularly crucial segment.*

The program, as previously mentioned, is extremely simple to interact with as the user simply needs to use the website created to input their job preferences, email address, and selecting whether they'd want to receive a new list the following week. After these inputs, the program will do the rest, including emailing the user the results.

The code behind the program is not so simple as it includes multiple facets. There are three components to the code: the webscraping of Indeed website, the weekly scheduling of the webscraping, and the emailing of these results.

The program's first part of webscrapping was necessary as there were no free available APIs for any of the popular job boards used.

Following YouTuber Izzy Analytics' video (https://www.youtube.com/watch?v=eN_3d4JrL_w), we were able to accurately gather and retrieve all the information needed from Indeed's website after a job-specific search. The webscraping was split into two parts, scraping the job posts and then creating a csv file to log all the job posts. This had to be done separately, unlike Izzy's video, because in order to display the scraped results on the website, we resorted to creating a function that logs the job post information into a dictionary for easy identification and accessibility. However, this dictionary could not be transformed easily into a csv file for the purposes of emailing the results to the user so we altered the function slightly to log the search results into a list to convert it into a csv.

The main function is the final function that ties all the multiple webscraping functions together.

*Insert image of the most important function - Photo 1*

The second part of the project was understanding how to schedule the webscraping to repeat after a certain given time. Our group decided that we'd give the user the option to select scheduling the webscraping weekly. Using the https://dev.to/bhupesh/a-simple-scheduler-in-python-49di article on scheduling, we were able to create the send_jobs function that would have scheduling off as a default unless the user selects "yes" aka "True", then the program would be scheduled weekly.

*Insert image of the send_job function - Photo 2*

The third part of the project was the emailing of the results. This part was extremely important as it was also the method that joined all the code and html together. It took into account the webscraping results and scheduling preerences that initially came from the user website and using an html email template, sent the user the results. We utilized multiple sources to create this function as well as help from Professor Zhi Li.

*Insert image of the email function - Photo 3*

## Results
**(DELETE)***Though the details will be different for each project, show off what your software can do! Screenshots and video are likely helpful. Include graphs or other data if appropriate.*

Here is a look at the results achieved by this program.

1. Here are the webscraping results that the code brings:

*Insert image of the CSV results file - Photo 4*

2. The CSV file's information is then sent as an email to the user:

*Insert Image of the Email Sent to User - Photo 5*

Now, it is important to note that in theory the scheduling code should work, however, it was never tested on the weekly basis as it would require the computer constantly on and running. This is an area that still needs work and would be something we would have researched further and implemented, if there was more time. Figuring out how to have the program running for a week in the background would be the next thing we'd tackle.

As a group, there are multiple results that we've achieved:

1. **Successful Pair Programming**: We worked together as a team, pair programming on multiple facets of the project where we learned visual code tips and tricks from each other, brainstormed implementation methods as a team, and were able to bypass challenges with each other's help.
   
2. **Learned Webscraping**: While our team varies in webscrapping abilities, we all learned  a little about it (this was dependent on our responsibilities on the team).

3. **Scheduling and emailing**: We learned how to use Python to schedule code and send emails.

## Project Evolution
  *Tell an illustrative story about the process of creating your software, showing how it improved over time. This may draw upon what you learned from the two peer technical reviews. Consider the use of screenshots or other tools to demonstrate how your project evolved.*

The Automated Job Searcher has evolved plenty since the start of the project. In the beginning the idea was to use a website's API to get information, have a database that holds usernames and passwords for users, and to use that database to store all the jobs already sent so that each week only new jobs are sent. What we learned is that while these are great ideas, we first needed to scale down our idea to the bare minimum with one user in mind *and then* build from there.

As previously mentioned, we tried finding job board APIs that were free, but unfortunately, none could be found. Instead, we found a video tutorial on how to webscrape Indeed that we ended up using (please refer to Attribution for source). We've built this program now with one user at a time using this program. We also decided it would be easier to send all the results received each week and not cross check them as that can become complicated as we involve more users into the situation.

In the future we'd have to work on how the program responds when multiple users are on the website giving their information and preferences in - at that time we might need to create a database for holding email addresses and preferences to create a list of the webscraping our code must do and in what order. In addition, we'd also have to work on how to keep the scheduling automated and in the background. Most importantly, webscraping Indeed is a little iffy so if this project were to move forward we would definitely work with Indeed to receive an API. That was not possible right now as Indeed was no longer recieving applications for using their API. However, with all of these "next tasks" that we have, we are proud of all that we have been able to acheive.

## Attribution (Work Cited)
**(DELETE)***all work cited*

This project could not have been done without the help of our Professor Zhi Li and these sources below that helped in various parts of our project.

Source for webscraping indeed: https://www.youtube.com/watch?v=eN_3d4JrL_w
Source for bs4 documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
Source for scheduling: https://dev.to/bhupesh/a-simple-scheduler-in-python-49di
Source for Emailing:
- https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/#Sending_HTML_email
- https://dev.to/carola99/send-an-html-email-template-with-python-and-jinja2-1hd0
- https://www.spritecloud.com/creating-and-sending-html-e-mails-with-python/ 