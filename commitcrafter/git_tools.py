from git import Repo


def get_latest_diff():
    repo = Repo(".")
    hcommit = repo.head.commit
    diff = hcommit.diff("HEAD~1", create_patch=True)
    diff_text = "".join([d.diff.decode() if d.diff else "" for d in diff])
    return diff_text


print(get_latest_diff())
