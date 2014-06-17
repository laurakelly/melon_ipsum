from random import choice
from sys import argv

melon_words = [
    "watermelon",
    "watermelon",
    "watermelon",
    "melon",
    "melon",
    "melon",
    "honeydew",
    "ripe",
    "juicy",
    "sweet",
    "White Sugar Lump",
    "vine",
    "Jubilee Bush",
    "Golden Honey",
    "melon",
    "fresh",
    "Armenian Cucumber",
    "as a service",
    "as a service",
    "in real-time",
    "in real-time",
    "disrupting the melon-sphere",
    "disrupting the melon-sphere",
    "drive-by fruiting",
    "using the latest technology",
    "right at your fingertips",
    "using our innovative fruit-prediction algorithm",
    "we deliver",
    "melons when you need them",
    "Jubilee",
    "Navajo Winter",
    "Missouri Heirloom",
    "Mountain Hoosier",
    "Orange Flesh Tendersweet",
    "Irish Grey",
    "Long Milky Way",
    "Moon and Stars", 
    "Densuke",
    "Thai Rom Dao",
    "Cantaloupe",
    "Ali Baba",
    "Peacock Striped",
    "Cream of Saskatchewan",
    "Daisy or Yellow Shipper",
    "Mississippi Cobb Gem",
    "Black Diamond Yellow-Belly Strain",
    "Japanese Cream Fleshed Suika",
    "Casaba",
    "Hopi Yellow",
    "Wilson's Sweet",
    "Desert King",
    "Chris Cross",
    "Golden Midget",
    "Sugar Baby",
    "Scaly Bark",
    "Orangeglo",
    "Christmas",
    "Crimson Sweet"
]

def create_paragraph():
    # pick number of sentences in the paragraph
    num_sentences = choice([4,5,6,7])

    paragraph = ""
    for i in range(num_sentences):
        paragraph += create_sentence()

    return paragraph

def create_sentence():
    # pick number of words in the sentence
    num_words = choice([5,6,7,8])

    sentence = ""
    for i in range(num_words):
        sentence = sentence + " " + choice(melon_words)

    sentence = sentence.lower()
    sentence = sentence[1].upper() + sentence[2:] 
    return sentence + ". "

def main():
    num_paragraphs = argv[1]

    melon_ipsum = ""

    for i in range(int(num_paragraphs)):
        melon_ipsum += create_paragraph()
        melon_ipsum += "\n"

    print melon_ipsum

    

if __name__ == "__main__":
    main()
