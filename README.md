# EchoBot

Bot Framework v4 echo bot sample.

This bot has been created using [Bot Framework](https://dev.botframework.com), it shows how to create a simple bot that accepts input from the user and echoes it back.

## To try this sample

- Clone the repository
```bash
git clone https://github.com/Microsoft/botbuilder-samples.git
```
- In a terminal, navigate to `botbuilder-samples\samples\python\02.echo-bot` folder
- Activate your desired virtual environment
- In the terminal, type `pip install -r requirements.txt`
- Run your bot with `python app.py`

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the latest Bot Framework Emulator from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- File -> Open Bot
- Enter a Bot URL of `http://localhost:3978/api/messages`

## Interacting with the bot

Enter text in the emulator.  The text will be echoed back by the bot.

## Deploy the bot to Azure

To learn more about deploying a bot to Azure, see [Deploy your bot to Azure](https://aka.ms/azuredeployment) for a complete list of deployment instructions.

## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Channels and Bot Connector Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)


## EchoBot with Azure Cognitive Services Integration
- This sample bot demonstrates how to integrate a chatbot with Azure Cognitive Services, specifically using - - Azure Text Analytics for sentiment analysis. It builds upon the EchoBot sample provided by Bot Framework v4.
## Prerequisites
- Before running this sample, ensure you have the following:
- Python 3.6 or later installed
- An Azure account with Azure Cognitive Services provisioned
## Configuration
- Clone the repository:
- git clone (https://github.com/Microsoft/botbuilder-samples.git)
- Navigate to the EchoBot folder:
- 'cd botbuilder-samples/samples/python/02.echo-bot'
- Install dependencies:
- 'pip install -r requirements.txt'
## Set up environment variables:
- MicrosoftAppId: Your bot's Microsoft App ID
- MicrosoftAppPassword: Your bot's Microsoft App Password
- MicrosoftAIServiceEndpoint: The endpoint URL for Azure Cognitive Services (default: https://lang-s01.cognitiveservices.azure.com/)
- MicrosoftAPIKey: Your API key for Azure Cognitive Services (default: d8c4f1a683a345428afbbad03de671cf)
## Running the bot
- 'python app.py'
## Interacting with the bot
- Once the bot is running, you can interact with it via a bot framework emulator or any client application that can send HTTP requests.
## Bot Functionality
- The bot echoes back any input it receives from the user. Additionally, it performs sentiment analysis on the input text using Azure Cognitive Services and returns the sentiment analysis results.
## Deploying the Bot to Azure
- To deploy the bot to Azure, follow the deployment instructions provided by Microsoft's Azure Bot Service documentation.
## Resources
- (https://docs.botframework.com/)
- (https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- (https://docs.microsoft.com/azure/cognitive-services/?view=azure-services)
- (https://github.com/microsoft/botframework-emulator)
- (https://portal.azure.com/)
- (https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)











