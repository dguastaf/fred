import { Text, TouchableOpacity } from "react-native";

interface GoogleAuthButtonProps {
  onPress: () => void;
}

export default function GoogleAuthButton({ onPress }: GoogleAuthButtonProps) {
  return (
    <TouchableOpacity
      onPress={onPress}
      className="bg-blue-500 px-6 py-3 rounded-lg mt-4 active:bg-blue-600"
    >
      <Text className="text-white font-semibold text-center">
        Authenticate with Google Calendar
      </Text>
    </TouchableOpacity>
  );
}
