import json
import os

def add_hidden_community(category_name, community):
    with open("hidden-communities.json", "r") as f:
        categories = json.load(f)

    category = categories.get(category_name, categories.get("other"))
    category.append(community)

    with open("hidden-communities.json", "w") as f:
        json.dump(categories, f, indent=2)


def unpack_instances(community_list):
    instances = {}
    for community in community_list:
        instance = community.split("@")[1]
        if instance not in instances:
            instances[instance] = []
        instances[instance].append(community)
    return instances

def generate_hidden_communities():
    with open("hidden-communities.json", "r") as f:
        categories = json.load(f)
    print("""# Hidden Communities

This document details hidden communities aka communities that are marked to not show up by default on the site.

Programming.dev will hide political communities, advertising/spam communities, NSFW/pornographic communities and communities that have a majority of their content produced by bots. While a community is hidden, it and its posts and comments will not show up in post feeds or in the search results unless you have explicitly subscribed to it. Communities themselves currently do not show up in community search results, this may change in the future; see [#2943](https://github.com/LemmyNet/lemmy-ui/issues/2943).

Users can subscribe to a hidden community to remove the hidden effect status of a community, however it can be difficult for a user to find out which communities are due to them not being searchable. This page aims to provide more transparency to our users of which communities are hidden, and also give them a direct link to the community so that they can subscribe to the content if they wish. Some communities may be gone due to instances being shut down or by the local instance removing them; we do not update the list to reflect this.

**Programming.dev neither endorses nor condemns the content of these communities. Hidden communities are generally hosted on federated instances as programming.dev focuses primarily on programming-related content.**

## Hidden Communities
""")
    for category_name in categories.keys():
        instances = unpack_instances(categories[category_name])
        if len(instances) == 0:
            continue

        if category_name == "nsfw":
            print(f"### NSFW\n")
        if category_name == "bots":
            print(f"### Bot Communities\n")
        if category_name == "political":
            print(f"### Political Communities\n")
        if category_name == "spam":
            print(f"### Spam/Advertising Communities\n")
        if category_name == "test":
            print(f"### Test Communities\n")
        if category_name == "other":
            print(f"### Other\n")

        for instance in sorted(instances.keys(), key=str.casefold):
            print(f"- {instance}")
            communities = sorted(instances[instance], key=str.casefold)
            for community in communities:
                print(f"  - [{community}](https://programming.dev/c/{community})")
            print()

"""
Usage:

    python hidden_communities.py generate > hidden-communities.md

    python hidden_communities.py add <category> <community>

        Category: nsfw, bots, political, spam, test, other
        Community: Must include instance name, e.g. "test@programming.dev"
"""
if __name__ == "__main__":
    args = os.sys.argv
    args.pop(0)
    command = args.pop(0)
    if command == "generate":
        generate_hidden_communities()
    elif command == "add":
        if len(args) != 2:
            print("""
python hidden_communities.py add <category> <community>

Category: nsfw, bots, political, spam, test, other
Community: Must include instance name, e.g. "test@programming.dev"
            """)
            exit(-1)
        category_name = args.pop(0)
        community = args.pop(0)
        if "@" not in community:
            print("""
Invalid Community:

Must include instance name, e.g. "test@programming.dev"
            """)
            exit(-1)
        instance = community.split("@")[1]
        add_hidden_community(category_name, community)
