from git import Repo


def get_latest_diff(repo_path: str, compare_to: str = None) -> str:
    """
        Get the latest diff from the git repository at the given path.
        Args:
        repo_path (str): The path to the git repository.
        compare_to (str): The commit to compare the latest commit to.
    """
    repo = Repo(repo_path, search_parent_directories=True)
    hcommit = repo.head.commit
    diff = hcommit.diff(compare_to, create_patch=True)
    diff_text = "".join([d.diff.decode() if d.diff else "" for d in diff])
    return diff_text
