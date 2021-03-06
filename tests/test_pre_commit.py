import re
import subprocess

from test_cookie import basic_project_dict


def _check_pre_commit(result):
    subprocess.check_output(("pre-commit", "install"), shell=True, cwd=result.project)

    c = subprocess.Popen(
        "pre-commit run --all-files",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        cwd=result.project,
    )
    output, error = c.communicate()

    failure = re.search(r"Failed", str(output))
    if failure is not None:
        print(output)
        raise AssertionError("Some pre-commit failed.")
    # Not trivial to check for empty string if it might be binary stream
    assert len(error) == 0, "{}".format(str(error))
    assert re.search(
        r"(Passed|Failed)", str(output)
    ), "All files skipped by pre-commit."


def test_pre_commit_python_sphinx(cookies, basic_project_dict):
    basic_project_dict["set_up_git"] = "y"
    basic_project_dict["make_initial_commit"] = "y"
    basic_project_dict["add_basic_pre_commit_hooks"] = "y"
    basic_project_dict["add_intrusive_pre_commit"] = "y"
    basic_project_dict["configure_running_sphinx_from_waf"] = "y"
    result = cookies.bake(extra_context=basic_project_dict)
    _check_pre_commit(result)


def test_pre_commit_python(cookies, basic_project_dict):
    basic_project_dict["set_up_git"] = "y"
    basic_project_dict["make_initial_commit"] = "y"
    basic_project_dict["add_basic_pre_commit_hooks"] = "y"
    basic_project_dict["add_intrusive_pre_commit"] = "y"
    basic_project_dict["configure_running_sphinx_from_waf"] = "n"
    result = cookies.bake(extra_context=basic_project_dict)
    _check_pre_commit(result)


def test_pre_commit_r(cookies, basic_project_dict):
    basic_project_dict["set_up_git"] = "y"
    basic_project_dict["make_initial_commit"] = "y"
    basic_project_dict["add_basic_pre_commit_hooks"] = "y"
    basic_project_dict["add_intrusive_pre_commit"] = "y"
    basic_project_dict["example_to_install"] = "R"
    basic_project_dict["configure_running_r_from_waf"] = "y"
    result = cookies.bake(extra_context=basic_project_dict)
    _check_pre_commit(result)


def test_pre_commit_stata(cookies, basic_project_dict):
    basic_project_dict["set_up_git"] = "y"
    basic_project_dict["make_initial_commit"] = "y"
    basic_project_dict["add_basic_pre_commit_hooks"] = "y"
    basic_project_dict["add_intrusive_pre_commit"] = "y"
    basic_project_dict["example_to_install"] = "Stata"
    basic_project_dict["configure_running_stata_from_waf"] = "y"
    result = cookies.bake(extra_context=basic_project_dict)
    _check_pre_commit(result)


def test_pre_commit_julia(cookies, basic_project_dict):
    basic_project_dict["set_up_git"] = "y"
    basic_project_dict["make_initial_commit"] = "y"
    basic_project_dict["add_basic_pre_commit_hooks"] = "y"
    basic_project_dict["add_intrusive_pre_commit"] = "y"
    basic_project_dict[
        "example_to_install"
    ] = "Julia (Warning: You will need to fix a lot yourself! Patches welcome!)"
    basic_project_dict["configure_running_julia_from_waf"] = "y"
    result = cookies.bake(extra_context=basic_project_dict)
    _check_pre_commit(result)


def test_pre_commit_matlab(cookies, basic_project_dict):
    basic_project_dict["set_up_git"] = "y"
    basic_project_dict["make_initial_commit"] = "y"
    basic_project_dict["add_basic_pre_commit_hooks"] = "y"
    basic_project_dict["add_intrusive_pre_commit"] = "y"
    basic_project_dict["example_to_install"] = "Matlab"
    basic_project_dict["configure_running_matlab_from_waf"] = "y"
    result = cookies.bake(extra_context=basic_project_dict)
    _check_pre_commit(result)
