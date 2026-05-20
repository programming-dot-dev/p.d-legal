import json
import os

def generate_hidden_communities():
    with open("hidden-communities.json", "r") as f:
        categories = json.load(f)
    with open("hidden-communities.md", "w") as w:
        w.write("""# Hidden Communities

This document details hidden communities aka communities that are marked to not show up by default on the site.

Programming.dev will hide political communities, advertising/spam communities, NSFW/pornographic communities and communities that have a majority of their content produced by bots. While a community is hidden, it and its posts and comments will not show up in post feeds or in the search results unless you have explicitly subscribed to it. Communities themselves currently do not show up in community search results, this may change in the future; see [#2943](https://github.com/LemmyNet/lemmy-ui/issues/2943).

Users can subscribe to a hidden community to remove the hidden effect status of a community, however it can be difficult for a user to find out which communities are due to them not being searchable. This page aims to provide more transparency to our users of which communities are hidden, and also give them a direct link to the community so that they can subscribe to the content if they wish. Some communities may be gone due to instances being shut down or by the local instance removing them; we do not update the list to reflect this.

**Programming.dev neither endorses nor condemns the content of these communities. Hidden communities are generally hosted on federated instances as programming.dev focuses primarily on programming-related content.**

## Hidden Communities

""")
        for category_name in categories.keys():
            if category_name == "nsfw":
                w.write(f"### NSFW\n\n")
            if category_name == "bots":
                w.write(f"### Bot Communities\n\n")
            if category_name == "political":
                w.write(f"### Political Communities\n\n")
            if category_name == "spam":
                w.write(f"### Spam/Advertising Communities\n\n")
            if category_name == "test":
                w.write(f"### Test Communities\n\n")
            if category_name == "other":
                w.write(f"### Other\n\n")
            instances = categories[category_name]
            for instance in sorted(instances.keys(), key=str.casefold):
                w.write(f"- {instance}\n")
                communities = sorted(instances[instance], key=str.casefold)
                for community in communities:
                    w.write(f"  - [{community}](https://programming.dev/c/{community})\n")

if __name__ == "__main__":
    generate_hidden_communities()