# Connections

The skills work with what they have and say plainly when something is missing. This is what each connection unlocks.

| Connection | Needed? | What you get | Without it |
|------------|---------|--------------|------------|
| Web search | Required | Finding roles, researching companies and interviewers | The plugin cannot find anything |
| A browser the agent can drive (Claude in Chrome, or the built-in browser in the desktop app) | Strongly recommended | Confirms a posting is really open by rendering the page | Postings are marked unverified instead of open |
| Gmail, read-only | Optional | Reads application confirmations, replies and job alert emails | You add applications to the tracker by hand |
| A spreadsheet or file skill | Recommended | Edits the tracker while keeping its formatting | The agent edits the file directly and is more likely to lose formatting |
| Calendar | Optional | Interview dates | You paste dates in |
| A connected drive, such as Google Drive | Optional | Reads your master resume from a document and saves tailored PDFs to a folder you name | You point the skill at a local file and folder instead |

## How to connect something

You do this yourself in your own Claude settings for connectors or tools. The agent cannot connect things for you. During setup it tells you what it can and cannot see in the current session.

## Gmail rules

The scan only calls tools that search or read mail. It never sends, replies, forwards, drafts, labels, archives or deletes. It asks each run, and a scheduled run skips email sweeps completely, because there is nobody there to say yes. If a Gmail tool in your setup cannot be restricted to read-only, leave Gmail unconnected and add applications by hand.

## Scheduled runs

A scheduled scan runs without you. It skips every email sweep. It also skips posting verification if no browser is available to it, and says so in the summary. Run the scan live when you want the full version.
