'''Question 5: Social Media Likes A social media platform stores the number of likes received by five posts in a list. Write a function to find the post with the highest likes, calculate total likes, and display posts that received at least 100 likes. 
'''


def SocialMedia(a):
    print("highest likes are:", max(a))

    print("total likes are:", sum(a))

    for _ in a:
        if _ >= 100:
            print("posts with at least 100 likes:", _)


a = [55, 180, 1050, 90, 10]

SocialMedia(a)