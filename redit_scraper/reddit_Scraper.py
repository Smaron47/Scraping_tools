# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService

# # Set the path to your chromedriver executable
# chrome_driver_path = "path/to/chromedriver"

# # Replace with your target URL
# url = "https://www.reddit.com/r/loseit/comments/18tghas/how_do_i_stop_overeating_without_developing_an_ed/"

# # Create a Chrome webdriver with non-headless mode
# chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = False
# driver = webdriver.Chrome(options=chrome_options)

# try:
#     # Open the URL in the browser
#     driver.get(url)
#     f=open('test.html','w')
#     f.write(driver.page_source)
#     f.close()
#     # Find all elements with the specified class using XPath
#     elements = driver.find_elements(By.XPATH, "//div[@class='py-0 mx-2xs xs:mx-sm inline-block max-w-full']")

#     # Print the text content of each element
#     for index, element in enumerate(elements, start=1):
#         text_content = element.text.strip()
#         print(f"Element {index} Text Content:", text_content)

# except Exception as e:
#     print("An error occurred:", str(e))

# finally:
#     # Close the browser window
#     driver.quit()




import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

# Set the path to your chromedriver executable
chrome_driver_path = "path/to/chromedriver"

# Replace with the URL of the subreddit you want to scrape
subreddit_url = "https://www.reddit.com/r/loseit/"

# Create a Chrome webdriver with non-headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)

# Open the subreddit URL in the browser
driver.get(subreddit_url)

try:
    # Simulate pressing Page Down 30 times
    for _ in range(13):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Add a delay to allow content to load (adjust if needed)

    # Find all post links using XPath
    post_links = driver.find_elements(By.XPATH, "//a[@slot='full-post-link']")
    
    post_links=[i.get_attribute("href") for i in post_links]
    # Create a CSV file to write the data
    #post_links = ['https://www.reddit.com/r/loseit/comments/18trs9j/official_weekly_foodie_friday_share_your_favorite/', 'https://www.reddit.com/r/loseit/comments/18tperq/are_tiktokers_lying/', 'https://www.reddit.com/r/loseit/comments/18trimc/my_people_deep_in_to_weight_loss_how_do_you_keep/', 'https://www.reddit.com/r/loseit/comments/18tpmfp/i_have_walked_500_miles/', 'https://www.reddit.com/r/loseit/comments/18txpln/gonna_do_the_damn_thing/', 'https://www.reddit.com/r/loseit/comments/18tijns/women_who_have_successfully_slimmed_down_cut_fat/', 'https://www.reddit.com/r/loseit/comments/18tmnue/gained_5lbs_over_christmas_little_disappointed_in/', 'https://www.reddit.com/r/loseit/comments/18trv3k/progress_yay_i_played_tag_with_my_nephew_neice/', 'https://www.reddit.com/r/loseit/comments/18tk3hf/the_more_weight_i_lose_the_more_i_realise_how/', 'https://www.reddit.com/r/loseit/comments/18ttb19/lost_weight_years_ago_gained_it_back_starting/', 'https://www.reddit.com/r/loseit/comments/18txwgt/thoughts_on_nyt_food_noise_oped/', 'https://www.reddit.com/r/loseit/comments/18tlh8r/should_i_strength_train_while_losing_weight_if_i/', 'https://www.reddit.com/r/loseit/comments/18td1yo/im_barely_eating_and_im_gaining_more_weight_idk/', 'https://www.reddit.com/r/loseit/comments/18txvro/30_day_accountability_challenge_day_29/', 'https://www.reddit.com/r/loseit/comments/18tk0uc/lost_20_kgs_and_still_have_lots_of_body_fat/', 'https://www.reddit.com/r/loseit/comments/18tuwxp/ive_lost_65_pounds_since_the_end_of_september/', 'https://www.reddit.com/r/loseit/comments/18tmow9/starting_2024_goals_a_couple_days_early/', 'https://www.reddit.com/r/loseit/comments/18tp5t5/the_more_i_try_the_more_i_fail_tired_of_it_all/', 'https://www.reddit.com/r/loseit/comments/18tyh84/new_years_resolutions/', 'https://www.reddit.com/r/loseit/comments/18tt8fq/i_give_up/', 'https://www.reddit.com/r/loseit/comments/18tpxml/learning_how_to_take_care_of_myself/', 'https://www.reddit.com/r/loseit/comments/18ty4nn/sharing_my_humble_calorie_counter_app/', 'https://www.reddit.com/r/loseit/comments/18tlobc/maintaining_weight_for_senior/', 'https://www.reddit.com/r/loseit/comments/18tufar/in_2024_i_am_breaking_free_from_sugar_addiction/', 'https://www.reddit.com/r/loseit/comments/18tx0w4/weight_gain_over_the_holidays/', 'https://www.reddit.com/r/loseit/comments/18ttl1d/beta_blockers_affect_on_metabolism_and_daily/', 'https://www.reddit.com/r/loseit/comments/18twd16/56_155_pounds_seriously_wanting_to_try_to_lose/']
    with open('reddit_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Post Name', 'Post Link', 'Content', 'Commenters', 'Comments Content'])

        # Iterate through each post link
        for post_link in post_links:
            try:
                post_href = post_link
                print(post_href)
                full_post_link = f'https://www.reddit.com{post_href}'

                # Open the post link
                driver.get(post_href)
                time.sleep(5)
                # Collect data from the post
                post_name = driver.find_element(By.XPATH, "//h1[@slot='title']").text.strip()
                print(post_name)
                content = driver.find_element(By.XPATH, '//div[@class="text-neutral-content"]').text.strip()
                #print(content)

                # Collect commenters and comments content
                commenters = driver.find_elements(By.XPATH, "//a[@class='truncate font-bold text-neutral-content-strong text-12 hover:underline']")
                #print(commenters)
                commenters_links = [commenter.get_attribute('href') for commenter in commenters]
                comments_content = driver.find_elements(By.XPATH, "//div[@class='py-0 mx-2xs xs:mx-sm inline-block max-w-full']")
                comments_content_list = [comment.text.strip() for comment in comments_content]

                # Write data to CSV file
                csv_writer.writerow([post_name, full_post_link, content, commenters_links, comments_content_list])
            except:
                pass
except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window
    time.sleep(60)
    driver.quit()
