# User Feedback

WorkflowAI allows you to collect feedback from users about your AI features.

{% hint style="info" %}
Collecting end user feedback is essential for understanding how your AI features perform in real-world scenarios. The main goal is to gather insights about user satisfaction and feature effectiveness when users interact with your AI agents in production environments. This data helps you identify strengths and weaknesses, prioritize improvements, and measure the overall health of your AI-powered features over time.
{% endhint %}

## Feedback loop
1. Add a feedback button to your product: using our web SDK, or by using our API.
2. Users click the button and give feedback.
3. Your team can view the feedback in the WorkflowAI dashboard.
4. Improve instructions based on the feedback.

## How it works

All you need to send feedback to WorkflowAI is the `feedback_token` that is provided when you call the `/run` endpoint. The `feedback_token` is a signed token that allows posting feedback to a single run. Once the feedback token is propagated to your client application, we have a couple of different ways to send feedback to WorkflowAI.

Optionally, you can also provide a `user_id` to track feedback per user. There can be only one feedback per (`feedback_token`, `user_id`) pair. So sending a new feedback for the same token / user ID pair will overwrite the existing ones.

[image]

### Access `feedback_token`

#### Python SDK

```python
...
```

#### Typescript SDK

```typescript
...
```

## Web SDK

The web SDK is the simplest way to add a feedback button to your web app.

### React

```bash
npm install @workflowai/react
```

```typescript
import { FeedbackButtons } from '@workflowai/react'

...
   <FeedbackButtons feedbackToken={...} userID={...} className='...'/>
...
```

## API

Use our API if you want full customization over the feedback button and send the feedback via your own backend.

### Python

```
python ...
```

### Typescript

```
ts ...
```

## View user feedback

Go to the "User Feedbacks" section from the menu, and you'll see a list of feedback.

[image]

{% hint style="info" %}
If you need any help, email us at team@workflowai.support or open a discussion on [GitHub](https://github.com/workflowai/workflowai/discussions).
{% endhint %}