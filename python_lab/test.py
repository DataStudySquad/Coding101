input="""
Born in Uganda, to Indian parents, Mamdani is a former rapper and the leading candidate in the November election. His heritage could resonate in the diverse city he hopes to lead.

Mamdani took a break from music when he first ran for office, winning a seat in the state assembly in 2020 representing Queens, the New York City borough with the largest Indian population.
"""

input2="""
Not every candidate for New York City mayor has rapped about having the same history as a chapati, or has convinced acclaimed food critic Madhur Jaffrey to perform in a video standing in a food truck, but Zohran Mamdani has.

Born in Uganda, to Indian parents, Mamdani is a former rapper and the leading candidate in the November election. His heritage could resonate in the diverse city he hopes to lead.

Mamdani took a break from music when he first ran for office, winning a seat in the state assembly in 2020 representing Queens, the New York City borough with the largest Indian population.

However, his past life in hip-hop remains a part of his official record. In his annual financial disclosures, the New York state assemblyman lists "self-employed rapper" as among his jobs and he still earns negligible royalties from performing under the names Young Cardamom and Mr. Cardamom.

Early in his music career, Mamdani performed as part of a duo with his childhood friend Hussein Abdul Bar at a music festival in their birthplace of Uganda in 2016.

Queen of Katwe, directed by Mamdani's mother, award-winning Indian filmmaker Mira Nair, had also just been released, along with a video for a song contributed by Mamdani.

The Disney opens new tab movie recounts the true story of a girl from a Ugandan slum who becomes a top chess player. Lupita Nyong'o and young actors from the movie appear in the music video.

"He would go on TV for interviews, or on radio for interviews, when his music video was going around on TV," said Derek Debru, a co-founder of the festival known as Nyege Nyege, which translates from Luganda as "urge to dance."

After meeting a hip-hop producer during the shooting of the movie, Mamdani recorded a few songs of his own.
"""

#print(words)
# array
# words = input.split(",")

# for i in range(len(words)):
#     print (words[i].strip()

def split_words(input):
    # array
    words = input.split(",")

    for i in range(len(words)):
        print (words[i].strip())

split_words(input2)