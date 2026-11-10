# Read-only existing-home recommendation

Existing CLEAN canonical home: `<HOME>/Dropbox/workspace/Le-AI-Lab/skills/omc-learned/paper-dev-review-layers-are-mandatory/SKILL.md`, section **Audit the review’s mathematics after its metadata passes** (starts line131). Read in full; path-specific Git status clean. No lab edits or new skill are proposed. Existing text already covers exact target binding and historical correction outcomes but does not state sibling module rebinding or distinguish previous-body equality from a newer current-body review.

Suggested bounded paragraph, appended to that section:

When any proof in a module changes, recompute the module hash for every current proof row in that file, including unchanged siblings. Keep current module/body/locator bindings separate from historical review bindings. Preserve previous reviewed-body hashes; a literal current-vs-previous equality flag is false when those bytes differ, even after a new review accepts the current body. Record exact matching to that newer review in its own binding field. Validate the complete current index against source, then apply metadata corrections by stable ID to the latest ledger without rewriting review history or grades.

This extends the existing review-binding rule and avoids creating a duplicate skill. Leave the dirty cited-theorem-source-fidelity-gate, focused-subscription-cli-review, repair-scope-swing-weak-to-circular and all unrelated WIP untouched.
