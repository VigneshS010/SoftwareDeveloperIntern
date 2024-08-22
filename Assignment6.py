# Web scraping using BS4 and Requests

import requests
from bs4 import BeautifulSoup


def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Check if the request was successful
        print(response)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Assuming headlines are under <h2> tags with a class "headline"
        headlines = soup.find_all('div', class_='B1S3_content__wrap__9mSB6')
        return [headline.get_text() for headline in headlines]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the data: {e}")
        return []


def display_headlines(headlines):
    if not headlines:
        print("No headlines found.")
    else:
        print("\nTop Headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")


def main():
    url = input("Enter the URL of the news website: ")
    headlines = fetch_headlines(url)
    display_headlines(headlines)


if __name__ == "__main__":
    main()

# Enter the URL of the news website: https://www.indiatoday.in/
# <Response [200]>
#
# Top Headlines:
# 1. Champai Soren amid BJP switch buzz: 'Was insulted, felt like I had no existence'Jharkhand Mukti Morcha leader Champai Soren said that he was not aware of the agenda of the meeting where he was asked to resign after Hemant Soren was released on bail, which was a "blow to self-respect".
# 2. Kolkata rape-murder victim's body cremated in haste, claims fatherThe rape and murder of a 31-year-old tainee doctor at a seminar hall of the government-run RG Kar Hospital in Kolkata last week has sparked widespread protests.
# 3. Bengaluru college student allegedly raped by biker who gave her liftThe 21-year-old woman, who is a college student, was returning home after a get-together. She took a lift from a biker, who instead of taking her to the designated place, took a detour to an isolated location, the police said.
# 4. How grocers' itch made Indian food win over American kitchensIndian grocery stores in the US are helping change the palettes of Americans by giving them a ready supply of Indian spices and ready-to-eat meals. Grocery stores like Patel Brothers, Triveni Supermarket, India Bazaar and Spice Bazaar are not just for Indians any more. This phenomenon has surprised celebrity chef Vikas Khanna too.
# 5. Rival football fans seeking justice for Kolkata rape victim lathicharged by policeFans of East Bengal and Mohun Bagan gathered outside Kolkata's iconic Salt Lake stadium despite the cancellation of the Durand Cup match between the clubs. They raised slogans demanding justice for the 31-year-old trainee doctor who was raped and murdered.
# 6. Hemant Soren's 'money is something' jibe amid Champai Soren's BJP switch buzzHemant Soren said that money is something that does not take long for leaders to switch sides. His remarks came amid growing speculation over his close aide Champai Soren mulling joining the BJP.
# 7. Arshad Warsi says Prabhas was like a 'joker' in 'Kalki'Arshad Warsi criticised 'Kalki 2898 AD', expressing his dislike for the film and comparing Prabhas to a 'joker.' The period drama was directed by Nag Ashwin.
# 8. Kolkata rape victim's father attacks Mamata Banerjee: 'Why the duplicity?'Father of the trainee doctor who was raped and killed at a Kolkata hospital claimed that the statewide movement over his daughter's death is being obstructed by the Bengal government. 
# 9. Kangana Ranaut calls Bollywood celebrities 'dumb': They can't talk beyond branded bagsActor Kangana Ranaut once again took a sly dig at Bollywood celebrities, calling them 'stupid and dumb,' and compared them to grasshoppers.
# 10. Top 10 Places to Visit in Gujarat During the MonsoonGujarat's monsoon season brings a refreshing transformation to its diverse landscapes. Whether you're drawn to hill stations, forests, dams, or eco-tourism sites, the rain enhances the natural beauty of these destinations.
# 11. 80 students hospitalised after eating biscuits at Maharashtra schoolAbout 80 students from a district council school in Chhatrapati Sambhajinagar district were hospitalised on Saturday after suffering nausea and vomiting from eating biscuits provided at their school.
# 12. Supreme Court takes note of Kolkata rape-murder, hearing on TuesdayA three-judge bench, comprising Chief Justice of India DY Chandrachud, Justices JB Pardiwala and Manoj Misra will hear the matter on Tuesday.
# 13. Flower seller forced to buy iPhone for son as he goes on hunger strike, Internet angryThe internet has slammed a flower seller's son after he went on a hunger strike to buy an iPhone.
# 14. Trinamool MP summoned after 'sniffer dog' claim against cops in rape-murder caseThe Kolkata Police has summoned senior Trinamool Congress leader Sukhendu Sekhar Ray for tweeting "wrong information" about the probe in connection with the RG Kar hospital rape and murder case.
# 15. UP teen alleges gangrape inside bus in Dehradun, 5 arrestedThe girl arrived in Dehradun on an Uttarakhand Roadways bus from Delhi. She was allegedly gang-raped on a bus by five men. Her medical examination has been conducted and a report is awaited.
# 16. Trinamool MP apologises for naming Kolkata rape victim, complaint filedRachana Banerjee recently posted a video on her social media handle condemning the incident. The name of the victim appeared at the end of the video.
# 17. When Jaya Bachchan said she's strict with Abhishek, not Aishwarya: She's not my daughter Jaya Bachchan once spoke about the difference between a daughter and a daughter-in-law. She also admitted to not being strict with Aishwarya Rai Bachchan.
# 18. Malayalam actor Mohanlal hospitalised due to breathing issuesMalayalam actor Mohanlal is hospitalised in Kochi after complaints of high fever and breathing troubles. The actor has been advised to avoid public spaces for five days along with medication.
# 19. Woman doctor assaulted by drunk patient, his relatives at Mumbai hospitalThe accused patient, with facial injuries and bleeding hands, came to Mumbai's Sion Hospital for treatment. As he was receiving treatment, he and his relatives started abusing and threatening the doctor.
# 20. Elon Musk compares Brazil's Chief Justice to Voldemort amid bitter X feudElon Musk compared Brazil's Chief Justice Alexandre de Moraes to Harry Potter villain Voldemort in a viral tweet. The post comes as Musk faces escalating tensions with Moraes, including threats to shut down X's operations in Brazil.
# 21. What your movie-watching etiquette says about youAre you the type who can't sit still during a movie, or do others' theatre antics drive you up the wall? Well, your movie-watching etiquette can reveal a lot about you.
# 22. Question Time: Weekly News QuizThink you read the headlines this week? Let's test that!
# 23. Air India crew member assaulted in London hotel room by intruder: ReportsThe attacker entered the Air India cabin crew member's room at the London hotel and physically assaulted her, hitting her with a clothes hanger before dragging her across the floor.
# 24. Kolkata rape-murder: What CBI asked ex-Principal of RG Kar hospitalThe CBI team investigating the rape and murder of the trainee doctor at RG Kar Medical College questioned the institute's former principal, Sandip Ghosh, for the third consecutive day.
# 25. 'The Tyrant' Review: Kim Seon-ho shines bright in this intense thrillerReleased-Wed Aug 14, 2024'The Tyrant' Review: The gripping Korean series race between the United States and South Korea to control a powerful bioweapon known as "The Tyrant Project" unfolds with high stakes and intense secrecy. Read the review to know more.
# 26. Watch: Kareena Kapoor, Saif Ali Khan exude royalty, hold hands at eventKareena Kapoor and Saif Ali Khan recently attended an event together in Mumbai. A video of the two has gone viral.
# 27. Arshad Warsi says Prabhas was like a 'joker' in 'Kalki'Arshad Warsi criticised 'Kalki 2898 AD', expressing his dislike for the film and comparing Prabhas to a 'joker.' The period drama was directed by Nag Ashwin.
# 28. Serendipity's Embrace Review: A wholesome K-Drama for your weekend bingeSerendipity's Embrace Review: If you are looking for a light-hearted and fun K-drama that is a breezy watch, the Chae Jong-hyeop and Kim So-hyun starrer is your pick.
#
# Process finished with exit code 0