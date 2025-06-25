import os


def save_history(history, test_name, keep_screenshot=False):
    output_dir = "browser_use_output"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, test_name.replace(' ', '_').lower() + ".json")
    if keep_screenshot is False:
        history = remove_screenshot(history)
    history.save_to_file(filename)
    return filename


def remove_screenshot(history):
    for step in history.history:
        if step.state.screenshot:
            step.state.screenshot = ""
    return history
