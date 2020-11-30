import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import email_schedule as es

"""Source for webscraping indeed: https://www.youtube.com/watch?v=eN_3d4JrL_w
    Source for bs4 documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
    Source for scheduling: https://dev.to/bhupesh/a-simple-scheduler-in-python-49di
    """


def search(position, location):
    """Creates a URL from a job position and a location"""
    position = position.replace(" ", "%20")
    location = location.replace(" ", "%20")
    # salary = salary.replace(",", "%2C")
    template = f"https://www.indeed.com/jobs?q={position}&l={location}"
    return template


# URL = search("data scientist", "New York")

# page = requests.get(URL)
# print(page)
# soup = BeautifulSoup(page.text, "html.parser")
# job_posts = soup.find_all("div", "jobsearch-SerpJobCard")
# # print(len(job_posts))

# job_post = job_posts[0]


def scrub_post(job_post, excel=False):
    """
    Scrubs the job board and collects the job post information
    """
    atag = job_post.h2.a
    job_title = atag.get("title")
    # print(job_title)
    job_url = "https://www.indeed.com" + atag.get("href")
    # print(job_url)
    company = job_post.find("span", "company").text.strip()
    # print(company)
    job_location = job_post.find("div", "recJobLoc").get("data-rc-loc")
    # print(job_location)
    job_summary = job_post.find("div", "summary").text.strip()
    # print(job_summary)
    post_date = job_post.find("span", "date").text
    # print(post_date)
    today = datetime.today().strftime("%Y-%m-%d")
    # print(today)
    try:
        salary = job_post.find("span", "salaryText").text.strip()
    except AttributeError:
        salary = ""
    if excel is True:
        result = [
            job_title,
            company,
            job_location,
            salary,
            post_date,
            today,
            job_summary,
            job_url,
        ]
        return result
    else:
        result = {
            "job_title": job_title,
            "company": company,
            "job_location": job_location,
            "salary": salary,
            "post_date": post_date,
            "today": today,
            "job_summary": job_summary,
            "job_url": job_url,
        }
        return result


# results = []

# for job in job_posts:
#     result = scrub_post(job)
#     results.append(result)

# print(results)


"""Navigating to the next page
while True:
    try:
        URL = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get(
            "href"
        )
    except AttributeError:
        break
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    job_posts = soup.find_all("div", "jobsearch-SerpJobCard")

    for job in job_posts:
        result = scrub_post(job)
        results.append(result)"""


def find_jobs(position, location):
    """
    Scrubs job posts based on given position and location.

    Returns: CSV file of information.
    """
    results = {}
    URL = search(position, location)
    page_count = 0
    while page_count < 5:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        job_posts = soup.find_all("div", "jobsearch-SerpJobCard")

        id = 0
        while True:
            for job in job_posts:
                results[id] = scrub_post(job, False)
                id += 1
            break
        page_count += 1
        try:
            URL = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get(
                "href"
            )
        except AttributeError:
            break

        return results


# results = main("data scientist remote", "New York")
# print(results)


def write_csv(position, location):
    csv_results = []
    URL = search(position, location)
    page_count = 0
    while page_count < 5:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        job_posts = soup.find_all("div", "jobsearch-SerpJobCard")

        for job in job_posts:
            csv_result = scrub_post(job, True)
            csv_results.append(csv_result)
        page_count += 1
        try:
            URL = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get(
                "href"
            )
        except AttributeError:
            break
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "JobTitle",
                "Company",
                "Location",
                "Salary",
                "PostDate",
                "DateRetrieved",
                "Summary",
                "JobUrl",
            ]
        )
        writer.writerows(csv_results)


# write_csv(results)


def combine(position, location):
    write_csv(position, location)
    return main(position, location)


###TO USE IN WEBSITE
def schd_jobs(position, location, sched=False):
    results = find_jobs(position, location)
    write_csv(position, location)
    if sched == "yes" == True:
        schedule.every(1).weeks.do(combine(position, location))
        while True:
            schedule.run_pending()
            print("Waiting...")
    else:
        print("Done")
        return results


def main(position, location, schedule, recipient_email):
    content = schd_jobs(position, location, schedule)
    es.send_job_list(content, recipient_email, position, location)


if __name__ == "__main__":
    pass