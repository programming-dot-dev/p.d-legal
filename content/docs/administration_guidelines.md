# Administration Guidelines and User Information

This document details how the community and programming.dev's administration should interact. The first part of the document serves to inform our users on how they can contact the admin team if they want to file a complaint or have questions that might not be appropriate to ask on [meta@programming.dev](https://programming.dev/c/meta). The second part of the document is meant to serve as rules/guidelines for the administration team to follow when interacting with the community.

## Community transparency and accountability
This document is made publicly available so that the community may see what guidelines the administrators should follow. If you feel that an administrator has breached these guidelines, you are highly encouraged to contact another member of the administration team to file a complaint. Users may request that their complaint be anonymous. **This request will be treated as binding, and the administrator may under no circumstances deny anonymity or break this promise.**

### Channels to contact the programming.dev administration
Since some administrators have access to the database, there is no guarantee that the DMs between the complainant and an administrator may stay private. If the complainant fears that the administrator they wish to file a complaint on may snoop on their DMs, they are recommended to contact an administrator through a secure channel such as [Matrix](https://matrix.org/ecosystem/clients/).

### Contact list
Please prioritise contacting a community team member over non community team members.
- [Bugsmith (community team member)](https://programming.dev/u/bugsmith) Matrix channel: [@bugsmith_:matrix.org](https://matrix.to/#/@bugsmith_:matrix.org)
- [UlrikHD (community team member)](https://programming.dev/u/UlrikHD) Matrix channel: [@ulrikhd:matrix.org](https://matrix.to/#/@ulrikhd:matrix.org)
- [Ategon (development team lead)](https://programming.dev/u/Ategon) Matrix channel: [@ategon:matrix.org](https://matrix.to/#/@ategon:matrix.org)
- [Snowe (server owner)](https://programming.dev/u/snowe) Matrix channel: [@snowe:matrix.org](https://matrix.to/#/@snowe:matrix.org)


# Note: Content here and onwards are meant primarily for the administration team, but is left public for transparency.

## Definitions:

- **Strike**: a strike is a part of if the incremental [admin response system](#the-3-4-strike-system), where for each strike a user accumulate a stricter response is warranted, accumulating to a strike 4 response which would be a permanent ban.

- **Severity**: severity describes the minimum strike that should be applied to the offending content. E.g. content  of severity 2 should be given a minimum of strike 2, however if they are already at strike 2, the strike would increment to strike 3, etc...


## General Administration Guidelines
- The job of administrators is to maintain and develop programming.dev, both as a site and community, and to *strictly* enforce its rules and guidelines. It is not the job of the administrator to add their own flavour or personal rules when moderating the site. If an administrator feels there is a missing rule or guideline, they should always consult with the admin team before acting outside the guidelines stated at https://legal.programming.dev/
- Administrators are expected to comply with the [Code of Conduct](code-of-conduct.md) to the highest standard, this applies to both their admin account and any other accounts they have that links them to programming.dev.

  Acts that qualify to linking their alt-accounts with their admin account are as follows:
  - Accounts with identical name or references to their admin account, be it a local account or an account linked to programming.dev via the ActivityPub protocol.
  - They have revealed that they are an admin on programming.dev on their alt-account.
  - They have used their alt-account for administrative purposes on programming.dev.
  - They have referenced their alt-account on their admin account.
  - They have via any other way interleaved their alt-accounts such that someone interacting with their alt-account knows they are interacting with a programming.dev admin.
- It is recommended that administrators avoid getting into heated arguments with users. Administrators should as soon as they realise an argument is getting too heated or off-topic try to either de-escalate or disengage from the argument.
- If an administrator wishes to engage in controversial topics, it is recommended that they use an alternate account not linked to their admin account. While this is only a recommendation, it is a highly recommended one as the site has been drawn into needless admin drama with other instances as a result of this guideline not being followed in the past.
- Administrators are not allowed to moderate content they are personally entangled with. If a user posts a severe breach of the [Code of Conduct](code-of-conduct.md) that affects an administrator, the administrator should report the content and leave it to the rest of the admin team to handle. The administrator may not comment on the case unless questioned by the admin team and should under no circumstances suggest what action to take. The administrator is still allowed to temporarily remove the content if deemed necessary, such as in the instance of being doxxed, the administrator should however also immediately notify the admin team that they have taken such action. Breaking this *rule* is considered a severe breach of trust and power. Exceptions are made for CSAM, phishing attempts, or established spam/scam similar to the [Nicole spam](https://programming.dev/c/nicole@feddit.org).



## When to Perform Admin Actions
- As a general rule, administrators should leave moderation to moderators. If an administrator steps in on behalf of a moderator, they should follow the guidelines as laid out in [Acting on Behalf of Moderators](#acting-on-behalf-of-moderators).
- If user content is breaking the [Code of Conduct](code-of-conduct.md) and the severity is high enough to warrant admin action rather than waiting for mod action, the administrator should follow the protocol [Enforcing Programming.dev's Code of Conduct](#enforcing-programmingdevs-code-of-conduct) when deciding on what action to take. The boundary between when the severity is high enough for an administrator to step in and take action is purposefully left diffuse, but a guideline is that it at a minimum shouldn't be left to interpretation if the [Code of Conduct](code-of-conduct.md) has been breached or not.
- An administrator should never take administrative action on content that isn't strictly against our [Code of Conduct](code-of-conduct.md). If an administrator believes they've found content that requires administrative action, but isn't covered by the [Code of Conduct](code-of-conduct.md), they should always consult with rest of the admin team before taking action.
- If an administrator is not 100% sure if they should take action, they should consult with the rest of the admin team before taking action.
- Administrators should not moderate what federated users post on other federated instances. It sets a bad precedent and gives the admin team a workload it likely can't handle. We assume that federated instances comply with our [Defederation Policy](defederation-policy.md) and that administrators of the other instance will take action if necessary. Exceptions can be made for content of severity 4.
- Actions may be taken on our local users regardless of which instance they are interacting with, and on federated users that are interacting with our local users and communities.
- Admin moderated communities may be treated as site-wide communities, meaning that administrators may choose to apply admin actions instead of mod actions to content posted in those communities. This means that rather than banning someone from e.g. [programming@programming.dev](https://programming.dev/c/programming), they may ban them from the entire site. Such action should only be taken on content that breaks the [Code of Conduct](code-of-conduct.md). Breaches on community specific rules should still follow the guidelines in [Acting on Behalf of Moderators](#acting-on-behalf-of-moderators).


### Guidelines on Content Severity
- As general rule, administrators should apply charitable interpretations and not assume malice without good reason. The phrase *"remember the human"* should be in the back of the mind when analysing content, fights/arguments are rarely instigated without any explanation.
- We acknowledge that programming.dev will have users interacting with it with a wide spread of backgrounds, ages and social skills. It would be unreasonable to expect perfectly civil academic discussions, especially on subjective topics. As such, administrators are recommended to show leniency when applying CoC. 1.1 (Remember the Human), 3.2 (Ad Hominem), 3.5 (Hate Speech) and 3.7 (Encouraging Harm) for arguments that have gotten out of hand. While personal insults and attacks are still not allowed, one should take into account the contextual discussion when deciding on the severity. What might have normally warranted a strike 2, might be better suited as a strike 1.
- Unprompted or particularly severe breaches of CoC. 1.1 (Remember the Human), 3.2 (Ad Hominem), 3.5 (Hate Speech) and 3.7 (Encouraging Harm) such as using well established severe slurs or derogatory language, or telling someone with known metal health issues to kill themselves will normally warrant a strike 2 and removal of the offending content. For less offensive content, strike 1 may be issued.
- Breaches of Coc 3.4 (Unmarked Sensitive Content) and 3.6 (Vote Manipulation) are generally of severity 1. Do note that accidentally not marking sensitive content as NSFW should not be an immediate strike. Notify the user and give them time to correct their error. Refusal or repeated offences should be treated as an offence.
- Breaches for CoC, 3.1 (Doxxing), 3.8 (Unwelcome Sexual Advances) and 3.12 (Harassment) are generally of severity 2.
- Breach of Coc 3.3 (Impersonation) is always of severity 4 if the account is made for impersonation. If it's just someone lying with a normal non-offending account, it is left to the administrator to judge if it's a severity 2 or 4. Generally it should be a strike 2 if is a one-off lie.
- Breach of CoC 3.11 (Ban Evasion) is always of severity 4. Exceptions can be made if the user made a new account in an effort to get in contact with the administration team to appeal their ban, as this isn't directly trying to evade the ban.
- Posting spam may either be considered as a severity 2 or severity 4 offence. It is up to the administrator to judge whether the account posting spam is an account made solely to post spam (severity 4) or just an overly enthusiastic user that doesn't understand proper posting etiquette (severity 2).
- Posting copyright infringing material (US law) is generally of severity 1 or 2 depending on context. If the user is knowingly and maliciously posting copyrighted material, it is of severity 4. Copyright infringing material should always be removed, but the administrator is encouraged to explain what and why the content was removed to the user.
- Posting scams, CSAM, or other illegal material is always an immediate strike 4.
- Users who are knowingly trying to exploit the [3-4 strike system](#the-3-4-strike-system) should be given a strike 4. An administrator who wants to use this clause will need to provide sound reasoning to the admin team *before* issuing the strike.
- If an administrator stumbles upon content that isn't covered in the guidelines, it's recommended to discuss with the admin team before taking action. The document should also be updated afterward to cover the gap.

## Acting on Behalf of Moderators
When acting on behalf of moderators, administrators should only utilise the same tools that moderators have available. That means that site-wide bans are off the table, and actions taken should not be logged in the admin log. The administrator may act with a different level of discretion tailored to the specific community when acting as a moderator. This means that content that are agreed upon by the admin team to not be severe enough for administrative action, may still qualify for moderator action.

## Protocols

### The 3-4 Strike System
The strike system is incremental, a user on strike 2 will always lead to a minimum of a strike 3 regardless of the severity on their next violation. A user without any strikes may be given a strike of any severity, but it's *strongly* recommended that users with zero strikes are never directly given a strike 3 (temporary ban). Offences that don't warrant a direct permanent ban should at a minimum be given a warning before any temporary bans are issued. Users that are given a strike may be put under supervision to make sure they don't repeat an offence, this supervision may only last for as long as the user has a strike.  
A strike is decremented by 1 after 365 days without any further violations, for this specific purpose someone on strike 3.5 is treated as if they are on strike 3.

1\. For mild violations, a warning/reminder should be issued to the user in question and logged in the admin log.

2\. For a repeated or more severe violation, a warning should be issued, notifying that a repeated offence will result in a temporary site ban.

3\. After receiving a warning notifying the user of a potential ban, a repeated offence should result in a temporary site ban. Ban length is recommended to be between 4-14 days depending on the severity of the violations. E.g. 3 severity 1 violations may warrant a shorter ban that 2 severity 2 violations.
  
3.5. A user that has already received a temporary ban once, may be given an additional temporary ban and a final warning before incrementing to strike 4. Ban length is recommended to be between 14-30 days depending on the severity of the violations.

4\. If the user repeats a violation after a temporary ban, a permanent ban may be issued.

### Enforcing Programming.dev's Code of Conduct
If a user is found to be in violation of the [Code of Conduct](code-of-conduct.md), the following steps should be taken:

- Check if the user has previously been logged by another admin in the admin log, as of writing that would be #pd-warnings channel on discord.
- Enforce the 3-4 strike system based on previous history.
- Issue a warning to the user. It is recommended to issue the warning directly as a reply to the offending content, both for transparency, but also because some users may not properly receive DMs depending on the app they are using.
- It is left to the administrator's discretion if the offending content should be removed or not. In general, it is recommended to leave content untouched so that other users can see the context of the admin action, but it's ultimately left to the administrator to decide.


### Logging Admin Actions
Using whatever log system is currently in place, after an action is taken against a user, the administrator should log the following information:

- Add a new entry or update the entry with the following format as title: username@instance
- Provide a date and time of the action taken, and when the offending content was made. Format should be in ISO 8601.
- Provide a bullet point of the strike given.
- Provide a bullet point for the reason the action was taken. This could be reference to specific rules that are broken or a more general description of *why* the action was taken. For cases where interpretation may come at play, the administrator should explain their interpretation alongside their reason for taking action.
- Provide a copy of the offending content. This is to ensure a history of the offending content is recorded and easy to look up for future reference. Simply providing a link to the offending content is not acceptable as the content may be edited or removed, but it may be provided alongside the copy to provide further context. Content that is not text-based such as media files, or content that contains sensitive information such as doxxing, may instead be given a description of the content.
- Provide a copy of the message sent to the user as part of the admin action.
- Further data depending on context may be included.
