from git import Repo


def get_latest_diff(repo_path: str):
    repo = Repo(repo_path, search_parent_directories=True)
    hcommit = repo.head.commit
    diff = hcommit.diff(None, create_patch=True)
    diff_text = "".join([d.diff.decode() if d.diff else "" for d in diff])
    return diff_text
