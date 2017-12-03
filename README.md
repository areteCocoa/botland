With the release of iOS 11.1, Apple introduced a bug that occurred when using the default keyboard. Specifically, autocorrect would suggest replacing occurrences of "i" with what would initially appear to be an "A" followed by a question mark inside a square. Autocorrect was appending a Variation Selector 16 character which is supposed to cause the previous character to have an emoji appearance. For "i", the selector is invalid so the correct behavior is undefined. The appearance of the malformed character sequence varies depending on the particular application that is attempting to display it.

This bot monitors the reddit comment stream for instances where the malformed character sequence appears and, when found, suggests that the user upgrade their iOS to the latest verion to fix the problem.

See the following article for a more detailed explanation: https://blog.emojipedia.org/why-ios-is-spreading-question-mark-boxes/
