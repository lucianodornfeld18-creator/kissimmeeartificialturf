# Twilio voice flow for (689) 202-3710

Same shape as `ocoee-voice` and `kissimmee-voice` on the account:

    caller dials (689) 202-3710
      -> /incoming   "Welcome to Kissimmee Artificial Turf. This call may be recorded. Press any key to speak with our team."
                     (said twice at 85% speed; no key = hang up, which screens robocalls)
      -> dials FORWARD_TO with the caller's number as caller ID, 20 s timeout, dual-channel recording
      -> /whisper    owner hears "New lead from Kissimmee Artificial Turf. Press any key to accept."
      -> /accept     empty TwiML bridges the two legs
      -> /voicemail  nobody accepted: "Sorry we missed your call..." + 120 s recording with transcription

The "this call may be recorded" sentence is there because Florida requires all-party consent to record a call (F.S. 934.03).

## Deploy

Credentials are never stored in this repo. From a shell:

    set TWILIO_SID=ACxxxxxxxx
    set TWILIO_TOKEN=xxxxxxxx
    set FORWARD_TO=+1XXXXXXXXXX      (optional; defaults to the Orlando hubs' owner line)
    python twilio/deploy_kissimmeeturf_voice.py

The script creates the Serverless service `kissimmeeturf-voice`, uploads the four protected functions, builds, creates the `prod`
environment, sets `TWILIO_NUMBER` and `FORWARD_TO`, deploys, and points the number's Voice URL at `/incoming`.
It is safe to re-run. `functions/*.js` in this folder are a readable copy of what the script uploads.

## Verify without a paid call

POST to each handler with an `X-Twilio-Signature` header computed as base64(HMAC-SHA1(auth_token, url + sorted key+value pairs)):
unsigned request -> 403; `/incoming` without Digits -> Gather with the greeting; with `Digits=1` -> Dial to FORWARD_TO;
`/whisper` -> the lead announcement; `/voicemail` in its three states. Then place one real call and confirm the recording and transcription.
