import { Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import GoogleAuthButton from "./components/GoogleAuthButton";

export default function Index() {
  return (
    <SafeAreaView className="flex-1">
      <View className="flex-1 items-center">
        <Text className="text-4xl font-bold">Fred! 🐙</Text>
        <GoogleAuthButton
          onPress={() => console.log("Google authentication pressed")}
        />
      </View>
    </SafeAreaView>
  );
}
