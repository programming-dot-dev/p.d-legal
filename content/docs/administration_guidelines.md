# Administration Guidelines and User Information

This document details how the community and programming.dev's administration should interact. The first part of the document servers as to inform normal users on how they can contact that admin team if they want to file a complaint or have questions they may not be fit to asking [meta@programming.dev](https://programming.dev/c/meta). The second part of the document is meant to serve as rules/guidelines for the administration team to follow when interacting with the community.

## Community transparency and accountability
This document is made publicly available so that the community may see by what guidelines the administrators should follow. If a user feel like an administrator has breached these guidelines when interacting with them, they are highly encouraged to contact another member of the administration to file a complaint. The user may request their complaint to be anonymous. **This request will be treated as binding, and the administrator may under no circumstances deny anonymity or break this promise.**

### Channels to contact the programming.dev administration
Since some administrators have access to the database, there is no guarantee that the DMs between the complainant and an administrator may stay private. If the complainant fear that the administrator they wish to file a complaint on may snoop on their DMs, they are recommend to contact an administrator through a secure channel such as matrix.

### Contact list
Please prioritise contacting a community team member over non community team members.
- [recursive_recursion (community team lead)](https://programming.dev/u/recursive_recursion) Matrix channel: [@recursive_recursion:matrix.org](https://matrix.to/#/@recursive_recursion:matrix.org)
- [Bugsmith (community team member)](https://programming.dev/u/bugsmith) Matrix channel: [@bugsmith_:matrix.org](https://matrix.to/#/@bugsmith_:matrix.org)
- [UlrikHD (community team member)](https://programming.dev/u/UlrikHD) Matrix channel: [@ulrikhd:matrix.org](https://matrix.to/#/@ulrikhd:matrix.org)
- [Ategon (development team lead)](https://programming.dev/u/Ategon) Matrix channel: [@ategon:matrix.org](https://matrix.to/#/@ategon:matrix.org)
- [Snowe (server owner)](https://programming.dev/u/snowe) Matrix channel: [@snowe:matrix.org](https://matrix.to/#/@snowe:matrix.org)


# Note: Content here and onwards are meant primarily for the administration team, but is left public for transparency.


## General Administration Guidelines
- The job of administrators is to maintain and develop programming.dev, both as a site and community, and to *strictly* enforce its rules and guidelines. It is not the job of the administrator to add their own flavour or personal rules when moderating the site. If an administrators feels there is a missing rule or guideline, they should always consult with the admin team before acting outside the guidelines stated in https://legal.programming.dev/
- Administrators are expected to comply with the [Code of Conduct](code-of-conduct.md) to the highest standard, this applies to both their admin account and any other accounts they have that links them to programming.dev.

  Acts that qualify to linking their alt-accounts with their admin account are as follows:
  - Accounts with identical name or references to their admin account, be it a local account or an account linked to programming.dev via the ActivityPub protocol.
  - They have revealed that they are an admin on programming.dev on their alt-account.
  - They have used their alt-account for administrative purposes on programming.dev.
  - They have referenced their alt-account on their admin account.
  - They have via any other way interleaved their alt-accounts such that someone interacting with their alt-account knows they are interacting with a programming.dev admin.
- It is recommended that administrators avoid getting into heated arguments with users. Administrators should as soon as they realise an arguments is getting too heated or off-topic try to either de-escalate or disengage from the argument.
- If an administrator wishes to engage in controversial topics, it is recommended that they use an alt-account not linked to their admin account. While this is only a recommendation, it is a highly recommended one as the site has be drawn into needless admin drama with other instances as a result of this guideline not being followed in the past.
- Administrators are not allowed under any circumstances to moderate content they are personally entangled with. If a user posts a severe breach of the [Code of Conduct](code-of-conduct.md) that affects an administrator, the administrator should report the content and leave it to the rest of the admin team to handle. The administrator may not comment on the case unless questioned by the admin team, and should under no circumstances suggest what action to take. The administrator is still allowed to temporarily remove the content if deemed necessary, such in the instance of being doxxed, the administrator should however also immediately notify the admin team that they have taken such action. Breaking this *rule* is considered a severe breach of trust of power. Exceptions are made for strike 4 breaches such CSAM or phishing attempts.



## When to Perform Admin Actions
- As a general rule, administrators should leave moderation to moderators. If an administrator steps in on behalf of a moderator, they should follow the guidelines as laid out in [Acting on Behalf of Moderators](#acting-on-behalf-of-moderators).
- If a user content is breaking the [Code of Conduct](code-of-conduct.md) and severity is high enough to warrant admin action rather than waiting for mod action, the administrator should follow the protocol [Enforcing Programming.dev's Code of Conduct](#enforcing-programmingdevs-code-of-conduct) when deciding on what action to take. The border between when the severity is high enough for an administrator to step in and take action is purposefully left diffuse, but a guideline is that it at a minimum shouldn't be left to interpretation if the [Code of Conduct](code-of-conduct.md) has been breached or not.
- An administrator should never take administrative action on content that isn't strictly against our [Code of Conduct](code-of-conduct.md). If an administrator believes they've found content that requires administrative action, but isn't covered by the [Code of Conduct](code-of-conduct.md), they should always consult with rest of the admin team before taking action.
- If an administrator is not 100% sure if they should take action, they should consult with the rest of the admin team before taking action.
- Administrators should not moderate what federated users post on other federated instances. It sets a bad precedent and gives the admin team a workload it likely can't handle. We assume that federated instances comply with our [Defederation Policy](defederation-policy.md) and that administrators of the other instance will take action if necessary. Exceptions can be made for content of strike 4 severity.
- Admin moderated communities may be treated as site-wide communities, meaning that administrators may choose apply admin actions instead of mod actions to content posted in those communities. This means that rather than banning someone from e.g. [programming@programming.dev](https://programming.dev/c/programming), they may ban them from the entire site. Such action should only be taken on content that breaks the [Code of Conduct](code-of-conduct.md). Breaches on community specific rules should still follow the guidelines in [Acting on Behalf of Moderators](#acting-on-behalf-of-moderators).


### Guidelines on Content Severity
- We acknowledge that programming.dev will have users interacting with it with a wide spread of backgrounds, ages and social skills. It would be unreasonable to expect perfectly civil academic discussions, especially on subjective topics. As such, administrators are recommended to show leniency when applying CoC. 1.1 (Remember the Human), 3.2 (Ad Hominem), 3.5 (Hate Speech) and 3.7 (Encouraging Harm) for arguments that have gotten out of hand. While personal insults and attacks are still not allowed, one should take into account the contextual discussion when deciding on the severity. What might have normally warranted a strike 2, might be better suited as a strike 1.
- Unprompted or particularly severe breaches of CoC. 1.1 (Remember the Human), 3.2 (Ad Hominem), 3.5 (Hate Speech) and 3.7 (Encouraging Harm) such as using well established severe slurs or derogatory language, or telling someone with known metal health issues to kill themselves will normally warrant a strike 2 and removal of the offending content.
- Breaches of Coc 3.4 (Unmarked Sensitive Content) and 3.6 (Vote Manipulation) are generally of severity 1.
- Breaches for CoC, 3.1 (Doxxing), 3.8 (Unwelcome Sexual Advances) and 3.12 (Harassment) are generally of severity 2.
- Breach of Coc 3.3 (Impersonation) is always of severity 4 if the account is made for impersonation. If it's just someone lying with a normal non-offending account, it is left to the administrator to judge if it's a strike 2 or 4. Generally it should be a strike 2 if is a one-off lie.
- Breach of CoC 3.11 (Ban Evasion) is always of severity 4. Exceptions can be made if the user made a new account in an effort to get in contact with the administration team to appeal their ban, as this isn't directly trying to evade the ban.
- Posting spam may either be considered as a strike 2 or strike 4 offence. It is up to the administrator to judge whether the account posting spam is an account made solely to post spam (strike 4 severity) or just an overly enthusiastic user that doesn't understand proper posting etiquette (strike 2 severity).
- Posting copyright infringing material (US law) is generally of severity 1 or 2 depending on context. If the user is knowingly and maliciously posting copyrighted material, it is of severity 4. Copyright infringing material should always be removed, but the administrator is encouraged to explain what and why the content was removed to the user.
- Posting scams, CSAM, or other illegal material is always an immediate strike 4.
- Users who are knowingly trying to exploit the [3-4 strike system](#the-3-4-strike-system) should be given a strike 4. An administrator who wants to use this clause will need to provide sound reasoning to the admin team *before* issuing the strike.
- If an administrator stumbles upon content that isn't covered in the guidelines, it's recommended to discuss with the admin team before taking action. The document should also be updated afterward to cover the gap.

## Acting on Behalf of Moderators
When acting on behalf of moderators, administrators should only utilise the same tools that moderators have available. That means that site-wide bans are off the table, and actions taken should not be logged in the admin log. The administrator may apply a looser interpretation of the [Code of Conduct](code-of-conduct.md) when acting as a moderator. This means that content that are agreed upon by the admin team to not be severe enough for administrative action, may still qualify for moderator action.

## Protocols

### The 3-4 Strike System
The strike system in incremental, a user on strike 2 will always lead to a minimum of a strike 3 regardless of the severity on their next violation. A user without any strikes may be given a strike of any severity, but it's *strongly* recommended that users with zero strikes are never directly given a strike 3. Offences that doesn't warrant a direct permanent ban should at a minimum be given a warning before any temporary bans are issued.

1\. For mild violations, a warning/reminder should be issued to user in question and logged in the admin log.

2\. For a repeated or more severe violation, a warning should be issued, notifying that a repeated offense will result in a temporary site ban.

3\. After receiving a warning notifying the user of a potential ban, a repeated offense should result in a temporary site ban.
  
3.5. A user that has already received a temporary ban once, may be given an additional temporary ban and a final warning before incrementing to strike 4 and be permanently banned from programming.dev.

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
- Provide a bullet point of the severity of the action taken.
- Provide a bullet point for the reason the action was taken. This could be reference to specific rules that are broken or a more general description of *why* the action was taken. For cases where interpretation may come at play, the administrator should explain their interpretation alongside their reason for taking action.
- Provide a copy of the offending content. This is to ensure a history of the offending content is recorded and easy to look up for future reference. Simply providing a link to the offending content is not acceptable as the content may be edited or removed, but it may be provided alongside the copy to provide further context.
- Provide a copy of the message sent to the user as part of the admin action.
- Further data depending on context may be included.
