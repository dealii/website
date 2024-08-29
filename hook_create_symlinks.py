import os

symlinks = [
    "large_assets/release-papers/deal83-preprint.pdf",
    "large_assets/release-papers/deal84-preprint.pdf",
    "large_assets/release-papers/deal85-preprint.pdf",
    "large_assets/release-papers/deal90-preprint.pdf",
    "large_assets/release-papers/deal91-preprint.pdf",
    "large_assets/release-papers/deal92-preprint.pdf",
    "large_assets/release-papers/deal93-preprint.pdf",
    "large_assets/release-papers/deal94-preprint.pdf",
    "large_assets/release-papers/deal95-preprint.pdf",
    "large_assets/workshops/workshop-2010",
    "large_assets/workshops/workshop-2012",
    "large_assets/workshops/workshop-2013",
    "large_assets/workshops/workshop-2015",
    "large_assets/workshops/workshop-2018",
    "large_assets/workshops/workshop-2019",
    "large_assets/workshops/workshop-2020",
    "large_assets/workshops/workshop-2021",
    "large_assets/workshops/workshop-2023",
    "large_assets/workshops/workshop-2024",
    "large_assets/images",
]

def on_post_build(**kwargs):
    "Post-build actions"

    config = kwargs['config']
    site_dir = config['site_dir']

    print("Putting symlinks in place")
    print("site_dir = ", site_dir)

    for src in symlinks:
        dst = os.path.basename(src)
        dst = os.path.join(site_dir, dst)
        print(dst, " -> ", src)
        os.symlink(src, dst)

